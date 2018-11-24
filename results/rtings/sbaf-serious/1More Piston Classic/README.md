# 1More Piston Classic

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 5.8; 28 5.2; 31 4.5; 34 3.8; 37 3.3; 41 2.6; 45 2.0; 49 1.5; 54 0.8; 60 -0.0; 66 -0.7; 72 -1.2; 79 -1.7; 87 -2.4; 96 -3.2; 106 -4.0; 116 -4.8; 128 -5.6; 141 -6.2; 155 -6.6; 170 -6.9; 187 -7.2; 206 -7.3; 227 -7.3; 249 -7.0; 274 -6.7; 302 -6.4; 332 -5.9; 365 -5.3; 402 -4.7; 442 -3.9; 486 -3.0; 535 -2.0; 588 -1.0; 647 -0.1; 712 0.5; 783 0.5; 861 0.1; 947 -0.1; 1042 0.3; 1146 1.0; 1261 1.4; 1387 1.7; 1526 2.1; 1678 2.9; 1846 4.1; 2031 5.1; 2234 5.9; 2457 6.0; 2703 6.0; 2973 4.8; 3270 2.6; 3597 1.0; 3957 -0.3; 4353 -2.2; 4788 -2.0; 5267 -0.9; 5793 0.4; 6373 0.9; 7010 2.1; 7711 0.3; 8482 0.0; 9330 -0.7; 10263 -0.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`1More Piston Classic GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `1More Piston Classic ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.73 | 6.3 dB  |
| Peaking | 202 Hz  | 0.62 | -7.9 dB |
| Peaking | 2691 Hz | 0.97 | 9.4 dB  |
| Peaking | 4238 Hz | 0.99 | -6.8 dB |
| Peaking | 6491 Hz | 2.6  | 3.3 dB  |
| Peaking | 209 Hz  | 2.68 | 0.5 dB  |
| Peaking | 395 Hz  | 1.5  | -1.0 dB |
| Peaking | 715 Hz  | 1.89 | 2.6 dB  |
| Peaking | 881 Hz  | 1.52 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/1More%20Piston%20Classic/1More%20Piston%20Classic.png)