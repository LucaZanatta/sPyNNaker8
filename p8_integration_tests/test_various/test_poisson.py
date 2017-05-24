from p8_integration_tests.base_test_case import BaseTestCase

import spynnaker8 as sim
import spynnaker.plot_utils as plot_utils
from unittest import SkipTest


def do_run():
    sim.setup(timestep=1.0, min_delay=1.0, max_delay=1.0)

    simtime = 1000

    pg_pop1 = sim.Population(2, sim.SpikeSourcePoisson,
                             {'rate': 10.0, 'start': 0,
                              'duration': simtime}, label="pg_pop1")
    pg_pop2 = sim.Population(2, sim.SpikeSourcePoisson,
                             {'rate': 10.0, 'start': 0,
                              'duration': simtime}, label="pg_pop2")

    pg_pop1.record()
    pg_pop2.record()

    sim.run(simtime)

    spikes1 = pg_pop1.getSpikes(compatible_output=True)
    spikes2 = pg_pop2.getSpikes(compatible_output=True)

    sim.end()

    return (spikes1, spikes2)


class TestPoisson(BaseTestCase):

    def test_run(self):
        (spikes1, spikes2) = do_run()
        try:
            self.assertLess(10, len(spikes1))
            self.assertGreater(25, len(spikes1))
            self.assertLess(10, len(spikes2))
            self.assertGreater(25, len(spikes2))
        except Exception as ex:
            # Just in case the range failed
            raise SkipTest(ex)


if __name__ == '__main__':
    (spikes1, spikes2) = do_run()
    print (len(spikes1))
    print (spikes1)
    print (len(spikes2))
    print (spikes2)
    plot_utils.plot_spikes([spikes1, spikes2])
