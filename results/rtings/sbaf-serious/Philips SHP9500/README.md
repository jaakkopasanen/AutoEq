# Philips SHP9500

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 5.8; 41 5.1; 45 4.3; 49 3.6; 54 2.8; 60 2.1; 66 1.5; 72 1.0; 79 0.7; 87 0.3; 96 -0.0; 106 -0.4; 116 -0.7; 128 -0.8; 141 -0.8; 155 -0.6; 170 -0.6; 187 -0.5; 206 -0.3; 227 0.1; 249 0.4; 274 0.6; 302 0.8; 332 0.9; 365 1.1; 402 1.0; 442 0.9; 486 1.0; 535 1.0; 588 0.9; 647 0.9; 712 0.8; 783 0.5; 861 0.2; 947 0.0; 1042 0.1; 1146 0.1; 1261 -0.3; 1387 -1.0; 1526 -1.3; 1678 -1.0; 1846 -0.5; 2031 0.7; 2234 1.8; 2457 1.5; 2703 0.2; 2973 0.0; 3270 0.9; 3597 1.0; 3957 -1.6; 4353 -3.0; 4788 -2.9; 5267 -1.3; 5793 -0.9; 6373 1.4; 7010 2.3; 7711 0.3; 8482 -1.1; 9330 -2.6; 10263 -0.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips SHP9500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips SHP9500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 1.04 | 6.9 dB  |
| Peaking | 3779 Hz | 1.84 | 3.8 dB  |
| Peaking | 4312 Hz | 2.42 | -6.2 dB |
| Peaking | 6769 Hz | 5.72 | 3.1 dB  |
| Peaking | 9112 Hz | 7.04 | -3.0 dB |
| Peaking | 48 Hz   | 2.2  | 1.0 dB  |
| Peaking | 147 Hz  | 0.88 | -1.7 dB |
| Peaking | 390 Hz  | 0.51 | 1.4 dB  |
| Peaking | 1736 Hz | 1.31 | -1.9 dB |
| Peaking | 2217 Hz | 4    | 2.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Philips%20SHP9500/Philips%20SHP9500.png)