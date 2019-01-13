# Rock Jaw Alpha Genus Black Filter (Left Channel Only, black filter in right ear faulty)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.2dB
GraphicEQ: 21 0.0; 23 -0.4; 25 -0.8; 28 -1.4; 31 -1.9; 34 -2.3; 37 -2.6; 41 -3.0; 45 -3.4; 49 -3.7; 54 -4.0; 60 -4.5; 66 -4.8; 72 -5.1; 79 -5.5; 87 -5.9; 96 -6.4; 106 -6.5; 116 -6.6; 128 -6.8; 141 -6.9; 155 -7.0; 170 -6.9; 187 -6.7; 206 -6.6; 227 -6.2; 249 -5.9; 274 -5.5; 302 -5.1; 332 -4.6; 365 -4.1; 402 -3.7; 442 -3.0; 486 -2.7; 535 -2.1; 588 -1.3; 647 -0.8; 712 -0.5; 783 0.2; 861 0.2; 947 0.2; 1042 -0.1; 1146 -0.6; 1261 -1.2; 1387 -2.2; 1526 -3.4; 1678 -4.4; 1846 -5.0; 2031 -5.4; 2234 -5.6; 2457 -5.5; 2703 -4.8; 2973 -2.5; 3270 0.2; 3597 2.1; 3957 1.0; 4353 -2.1; 4788 -4.8; 5267 -8.5; 5793 -7.6; 6373 -1.9; 7010 0.9; 7711 0.3; 8482 0.0; 9330 -1.4; 10263 -3.5; 11289 -1.2; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Rock Jaw Alpha Genus Black Filter (Left Channel Only, black filter in right ear faulty) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-21**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Rock Jaw Alpha Genus Black Filter (Left Channel Only, black filter in right ear faulty) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 108 Hz   | 0.52 | -6.0 dB  |
| Peaking | 255 Hz   | 1    | -3.0 dB  |
| Peaking | 2103 Hz  | 2.12 | -6.2 dB  |
| Peaking | 5463 Hz  | 5.98 | -10.1 dB |
| Peaking | 10158 Hz | 6.5  | -3.6 dB  |
| Peaking | 18 Hz    | 2.14 | 1.2 dB   |
| Peaking | 879 Hz   | 2.68 | 1.5 dB   |
| Peaking | 3637 Hz  | 3.59 | 7.0 dB   |
| Peaking | 3829 Hz  | 1.1  | -3.2 dB  |
| Peaking | 7130 Hz  | 3.74 | 2.8 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Rock%20Jaw%20Alpha%20Genus%20Black%20Filter%20(Left%20Channel%20Only,%20black%20filter%20in%20right%20ear%20faulty)/Rock%20Jaw%20Alpha%20Genus%20Black%20Filter%20(Left%20Channel%20Only,%20black%20filter%20in%20right%20ear%20faulty).png)