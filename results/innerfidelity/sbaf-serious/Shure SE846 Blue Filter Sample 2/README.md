# Shure SE846 Blue Filter Sample 2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -3.6; 23 -3.6; 25 -3.7; 28 -3.7; 31 -3.6; 34 -3.6; 37 -3.6; 41 -3.5; 45 -3.5; 49 -3.5; 54 -3.5; 60 -3.5; 66 -3.5; 72 -3.5; 79 -3.6; 87 -3.6; 96 -3.7; 106 -3.6; 116 -3.4; 128 -3.3; 141 -3.2; 155 -3.0; 170 -2.8; 187 -2.5; 206 -2.3; 227 -2.0; 249 -1.8; 274 -1.5; 302 -1.3; 332 -1.1; 365 -0.8; 402 -0.7; 442 -0.4; 486 -0.4; 535 -0.3; 588 0.2; 647 0.3; 712 0.4; 783 0.5; 861 0.3; 947 0.1; 1042 -0.2; 1146 -0.4; 1261 -0.6; 1387 -1.1; 1526 -1.3; 1678 -1.5; 1846 -1.3; 2031 -0.7; 2234 0.1; 2457 1.8; 2703 4.3; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 5.3; 4788 5.8; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE846 Blue Filter Sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE846 Blue Filter Sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 49 Hz   | 0.18 | -3.7 dB |
| Peaking | 702 Hz  | 0.79 | 1.1 dB  |
| Peaking | 1927 Hz | 1.14 | -3.7 dB |
| Peaking | 3218 Hz | 1.4  | 7.4 dB  |
| Peaking | 5613 Hz | 2.71 | 5.0 dB  |
| Peaking | 4590 Hz | 3.07 | 1.2 dB  |
| Peaking | 6548 Hz | 5.24 | 3.6 dB  |
| Peaking | 6739 Hz | 1.49 | -2.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Shure%20SE846%20Blue%20Filter%20Sample%202/Shure%20SE846%20Blue%20Filter%20Sample%202.png)