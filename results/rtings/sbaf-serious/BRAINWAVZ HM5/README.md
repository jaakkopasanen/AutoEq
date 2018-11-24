# BRAINWAVZ HM5

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.3dB
GraphicEQ: 21 0.0; 23 4.0; 25 3.8; 28 3.6; 31 3.4; 34 3.3; 37 3.2; 41 3.1; 45 3.0; 49 2.8; 54 2.6; 60 2.3; 66 1.9; 72 1.7; 79 1.5; 87 1.0; 96 0.5; 106 -0.1; 116 -0.6; 128 -1.0; 141 -1.3; 155 -1.3; 170 -1.2; 187 -1.2; 206 -1.0; 227 -0.6; 249 0.3; 274 1.7; 302 3.3; 332 4.8; 365 5.2; 402 4.4; 442 3.4; 486 2.4; 535 1.7; 588 1.0; 647 0.6; 712 0.6; 783 0.5; 861 0.4; 947 0.1; 1042 0.1; 1146 0.3; 1261 0.1; 1387 -0.5; 1526 -1.3; 1678 -2.0; 1846 -2.4; 2031 -2.2; 2234 -1.5; 2457 -0.9; 2703 -0.3; 2973 1.2; 3270 2.1; 3597 -0.8; 3957 -1.3; 4353 -2.4; 4788 -1.8; 5267 1.1; 5793 1.6; 6373 2.2; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`BRAINWAVZ HM5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-53**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `BRAINWAVZ HM5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 1.23 | 4.0 dB  |
| Peaking | 51 Hz   | 1.96 | 2.3 dB  |
| Peaking | 372 Hz  | 2.67 | 5.6 dB  |
| Peaking | 1874 Hz | 3.07 | -2.7 dB |
| Peaking | 6703 Hz | 7.41 | 4.0 dB  |
| Peaking | 166 Hz  | 0.94 | -4.6 dB |
| Peaking | 171 Hz  | 0.5  | 2.7 dB  |
| Peaking | 3172 Hz | 7.5  | 3.5 dB  |
| Peaking | 4688 Hz | 2.3  | -3.7 dB |
| Peaking | 5395 Hz | 4.55 | 3.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/BRAINWAVZ%20HM5/BRAINWAVZ%20HM5.png)