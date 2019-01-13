# AKG K619
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -4.5; 23 -4.6; 25 -4.7; 28 -4.8; 31 -4.9; 34 -4.9; 37 -4.9; 41 -4.9; 45 -4.8; 49 -4.7; 54 -4.4; 60 -4.1; 66 -3.6; 72 -2.9; 79 -2.0; 87 -0.8; 96 -0.7; 106 -0.7; 116 0.4; 128 1.6; 141 1.9; 155 2.8; 170 3.6; 187 3.6; 206 3.8; 227 3.8; 249 3.7; 274 3.7; 302 3.3; 332 2.8; 365 2.3; 402 1.8; 442 1.6; 486 1.1; 535 1.0; 588 1.1; 647 0.9; 712 0.6; 783 0.6; 861 0.3; 947 0.1; 1042 0.1; 1146 0.1; 1261 0.6; 1387 0.4; 1526 0.5; 1678 0.8; 1846 1.8; 2031 2.8; 2234 4.5; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K619 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K619 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.47 | -5.4 dB |
| Peaking | 207 Hz  | 0.96 | 5.8 dB  |
| Peaking | 211 Hz  | 2.83 | -1.4 dB |
| Peaking | 2896 Hz | 1.6  | 5.9 dB  |
| Peaking | 5235 Hz | 1.92 | 5.6 dB  |
| Peaking | 1473 Hz | 1.36 | -0.7 dB |
| Peaking | 2348 Hz | 7.28 | 1.6 dB  |
| Peaking | 6470 Hz | 5.5  | 2.9 dB  |
| Peaking | 7917 Hz | 2.03 | -2.4 dB |
| Peaking | 8457 Hz | 3.48 | 0.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K619/AKG%20K619.png)