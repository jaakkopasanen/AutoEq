# AKG K601 2007

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 5.8; 41 5.3; 45 4.8; 49 4.4; 54 4.0; 60 4.5; 66 5.1; 72 3.8; 79 2.8; 87 2.4; 96 1.6; 106 1.0; 116 0.7; 128 0.2; 141 -0.2; 155 -0.4; 170 -0.6; 187 -0.8; 206 -1.0; 227 -1.0; 249 -1.0; 274 -1.0; 302 -0.8; 332 -0.7; 365 -0.6; 402 -0.4; 442 -0.2; 486 -0.1; 535 0.1; 588 0.5; 647 0.5; 712 0.6; 783 0.3; 861 -0.1; 947 -0.1; 1042 -0.0; 1146 0.1; 1261 0.2; 1387 -0.1; 1526 -0.9; 1678 -1.5; 1846 -2.8; 2031 -3.7; 2234 -3.4; 2457 -3.2; 2703 -2.9; 2973 -2.1; 3270 -0.2; 3597 -1.0; 3957 -1.7; 4353 -2.4; 4788 -2.9; 5267 -1.3; 5793 -3.8; 6373 -5.0; 7010 -2.0; 7711 -2.4; 8482 -4.4; 9330 -4.5; 10263 -3.0; 11289 -0.9; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K601 2007 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K601 2007 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.65 | 6.5 dB  |
| Peaking | 2245 Hz | 1.98 | -3.7 dB |
| Peaking | 6103 Hz | 3.84 | -4.5 dB |
| Peaking | 8638 Hz | 4.1  | -2.2 dB |
| Peaking | 9520 Hz | 3.56 | -3.1 dB |
| Peaking | 68 Hz   | 4.24 | 2.3 dB  |
| Peaking | 235 Hz  | 0.76 | -1.5 dB |
| Peaking | 661 Hz  | 0.79 | 0.8 dB  |
| Peaking | 4618 Hz | 5.23 | -2.3 dB |
| Peaking | 5340 Hz | 7.52 | 1.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K601%202007/AKG%20K601%202007.png)