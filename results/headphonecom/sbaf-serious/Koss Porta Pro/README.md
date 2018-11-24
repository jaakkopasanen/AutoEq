# Koss Porta Pro

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 5.8; 31 5.0; 34 4.0; 37 3.2; 41 2.1; 45 1.2; 49 0.3; 54 -0.7; 60 -1.7; 66 -2.7; 72 -3.5; 79 -4.3; 87 -4.9; 96 -5.5; 106 -5.9; 116 -5.9; 128 -6.0; 141 -5.9; 155 -5.9; 170 -5.7; 187 -5.3; 206 -4.8; 227 -4.4; 249 -3.9; 274 -3.5; 302 -3.1; 332 -2.6; 365 -2.1; 402 -1.6; 442 -1.3; 486 -0.9; 535 -0.6; 588 -0.3; 647 0.0; 712 0.0; 783 0.2; 861 0.1; 947 0.0; 1042 -0.1; 1146 -0.3; 1261 -0.7; 1387 -1.4; 1526 -2.4; 1678 -3.3; 1846 -4.1; 2031 -4.7; 2234 -4.5; 2457 -3.0; 2703 -0.7; 2973 1.8; 3270 3.4; 3597 4.1; 3957 1.6; 4353 0.3; 4788 -1.2; 5267 1.0; 5793 4.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -0.5; 9330 -2.6; 10263 -0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -3.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss Porta Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss Porta Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.63 | 7.5 dB  |
| Peaking | 117 Hz  | 0.46 | -7.0 dB |
| Peaking | 2070 Hz | 1.1  | -8.7 dB |
| Peaking | 2133 Hz | 0.36 | 3.8 dB  |
| Peaking | 3284 Hz | 3.61 | 4.6 dB  |
| Peaking | 4801 Hz | 5.51 | -3.2 dB |
| Peaking | 6228 Hz | 4.89 | 5.3 dB  |
| Peaking | 9102 Hz | 4.8  | -3.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Koss%20Porta%20Pro/Koss%20Porta%20Pro.png)