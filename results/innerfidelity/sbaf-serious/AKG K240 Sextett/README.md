# AKG K240 Sextett
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 5.7; 37 4.9; 41 3.6; 45 2.5; 49 1.6; 54 0.6; 60 0.3; 66 0.6; 72 -0.7; 79 -3.4; 87 -5.1; 96 -6.1; 106 -6.6; 116 -6.9; 128 -6.9; 141 -6.6; 155 -6.3; 170 -4.7; 187 -5.0; 206 -5.5; 227 -5.1; 249 -4.7; 274 -4.2; 302 -3.8; 332 -3.4; 365 -2.8; 402 -2.6; 442 -2.1; 486 -1.5; 535 -2.0; 588 -1.9; 647 -1.5; 712 -1.2; 783 -0.6; 861 -0.3; 947 0.0; 1042 -0.1; 1146 -0.4; 1261 -0.6; 1387 -1.4; 1526 -2.2; 1678 -2.9; 1846 -3.4; 2031 -3.8; 2234 -3.1; 2457 -2.5; 2703 -0.1; 2973 3.3; 3270 2.1; 3597 1.4; 3957 -1.4; 4353 -6.1; 4788 -4.8; 5267 0.5; 5793 2.0; 6373 0.4; 7010 -3.2; 7711 -6.0; 8482 -9.2; 9330 -10.2; 10263 -6.0; 11289 -0.3; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K240 Sextett GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K240 Sextett ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 26 Hz    | 0.65 | 6.6 dB   |
| Peaking | 109 Hz   | 1.28 | -6.4 dB  |
| Peaking | 232 Hz   | 0.74 | -3.9 dB  |
| Peaking | 1919 Hz  | 3.01 | -3.9 dB  |
| Peaking | 8956 Hz  | 3.31 | -11.4 dB |
| Peaking | 2488 Hz  | 3.38 | -3.4 dB  |
| Peaking | 3080 Hz  | 2.34 | 5.3 dB   |
| Peaking | 4499 Hz  | 4.83 | -8.3 dB  |
| Peaking | 5691 Hz  | 5.12 | 4.3 dB   |
| Peaking | 11757 Hz | 6.17 | 2.1 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K240%20Sextett/AKG%20K240%20Sextett.png)