# AKG Y50
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.5; 25 5.1; 28 4.6; 31 4.3; 34 3.9; 37 3.5; 41 3.1; 45 3.0; 49 3.1; 54 3.2; 60 3.5; 66 4.0; 72 4.2; 79 4.2; 87 4.0; 96 4.0; 106 4.3; 116 4.6; 128 5.6; 141 6.0; 155 6.0; 170 6.0; 187 6.0; 206 6.0; 227 6.0; 249 5.6; 274 3.7; 302 2.3; 332 1.6; 365 1.5; 402 1.6; 442 1.6; 486 1.6; 535 1.4; 588 1.2; 647 1.0; 712 0.8; 783 0.6; 861 0.3; 947 0.1; 1042 -0.0; 1146 0.1; 1261 0.5; 1387 1.0; 1526 1.6; 1678 2.3; 1846 3.2; 2031 4.2; 2234 5.3; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 5.5; 3957 4.5; 4353 4.0; 4788 4.2; 5267 3.1; 5793 1.3; 6373 0.5; 7010 1.2; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG Y50 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG Y50 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.81 | 5.6 dB  |
| Peaking | 76 Hz   | 1.14 | 2.8 dB  |
| Peaking | 142 Hz  | 1.94 | 3.5 dB  |
| Peaking | 219 Hz  | 1.65 | 4.9 dB  |
| Peaking | 2985 Hz | 1.1  | 6.6 dB  |
| Peaking | 537 Hz  | 2.79 | 0.9 dB  |
| Peaking | 1107 Hz | 2.18 | -1.0 dB |
| Peaking | 2204 Hz | 3.57 | 1.1 dB  |
| Peaking | 4865 Hz | 4.41 | 2.2 dB  |
| Peaking | 5460 Hz | 0.61 | -0.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/AKG%20Y50/AKG%20Y50.png)