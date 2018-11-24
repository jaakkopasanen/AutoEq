# Swimbuds Swimbuds

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 1.1; 25 1.1; 28 1.2; 31 1.3; 34 1.3; 37 1.3; 41 1.4; 45 1.5; 49 1.5; 54 1.5; 60 1.3; 66 1.1; 72 1.1; 79 0.9; 87 0.7; 96 0.4; 106 -0.2; 116 -0.7; 128 -1.1; 141 -1.5; 155 -1.7; 170 -1.8; 187 -1.9; 206 -2.0; 227 -1.9; 249 -1.7; 274 -1.4; 302 -1.0; 332 -0.5; 365 -0.1; 402 0.7; 442 1.3; 486 2.0; 535 2.7; 588 3.0; 647 3.2; 712 2.9; 783 2.3; 861 1.5; 947 0.6; 1042 -0.4; 1146 -1.1; 1261 -1.0; 1387 -0.3; 1526 0.8; 1678 2.4; 1846 4.1; 2031 5.5; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Swimbuds Swimbuds GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Swimbuds Swimbuds ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 73 Hz   | 0.38 | 2.4 dB  |
| Peaking | 181 Hz  | 0.63 | -3.8 dB |
| Peaking | 611 Hz  | 1.23 | 3.6 dB  |
| Peaking | 1231 Hz | 1.92 | -4.5 dB |
| Peaking | 3121 Hz | 0.61 | 7.0 dB  |
| Peaking | 1604 Hz | 4.32 | -0.6 dB |
| Peaking | 2069 Hz | 3.47 | 1.3 dB  |
| Peaking | 3136 Hz | 2.3  | -1.0 dB |
| Peaking | 6170 Hz | 2.15 | 5.0 dB  |
| Peaking | 7605 Hz | 1.44 | -4.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Swimbuds%20Swimbuds/Swimbuds%20Swimbuds.png)