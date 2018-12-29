# SMS Over Ear ANC
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 4.5; 25 2.6; 28 -0.7; 31 -3.0; 34 -4.0; 37 -4.2; 41 -3.9; 45 -3.3; 49 -2.8; 54 -2.3; 60 -1.8; 66 -1.5; 72 -1.1; 79 -0.9; 87 -0.6; 96 -0.4; 106 -0.1; 116 0.3; 128 0.6; 141 0.8; 155 1.1; 170 1.5; 187 1.9; 206 2.3; 227 2.6; 249 2.9; 274 3.2; 302 3.6; 332 3.8; 365 4.1; 402 4.3; 442 4.8; 486 5.4; 535 5.7; 588 6.0; 647 5.7; 712 5.0; 783 4.2; 861 2.6; 947 1.0; 1042 -0.7; 1146 -2.0; 1261 -4.3; 1387 -7.7; 1526 -10.5; 1678 -11.9; 1846 -9.8; 2031 -6.7; 2234 -5.8; 2457 -3.7; 2703 -2.4; 2973 0.2; 3270 0.8; 3597 1.5; 3957 2.6; 4353 5.3; 4788 6.0; 5267 5.4; 5793 1.7; 6373 3.6; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SMS Over Ear ANC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SMS Over Ear ANC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 22 Hz   | 1.51 | 9.3 dB   |
| Peaking | 34 Hz   | 1.05 | -6.9 dB  |
| Peaking | 626 Hz  | 0.55 | 7.0 dB   |
| Peaking | 1630 Hz | 1.54 | -15.0 dB |
| Peaking | 4666 Hz | 1.86 | 6.7 dB   |
| Peaking | 745 Hz  | 2.7  | 0.8 dB   |
| Peaking | 1001 Hz | 2.23 | -1.3 dB  |
| Peaking | 1180 Hz | 3.31 | 1.0 dB   |
| Peaking | 6662 Hz | 6.17 | 4.1 dB   |
| Peaking | 6826 Hz | 2.22 | -2.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/SMS%20Over%20Ear%20ANC/SMS%20Over%20Ear%20ANC.png)