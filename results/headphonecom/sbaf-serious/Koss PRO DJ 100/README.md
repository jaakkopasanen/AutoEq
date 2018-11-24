# Koss PRO DJ 100

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 5.8; 34 5.4; 37 5.0; 41 4.5; 45 4.1; 49 3.7; 54 3.1; 60 2.4; 66 1.8; 72 1.6; 79 1.9; 87 1.1; 96 1.9; 106 0.1; 116 -0.9; 128 -1.8; 141 -2.5; 155 -3.1; 170 -2.9; 187 -3.8; 206 -4.0; 227 -4.1; 249 -4.2; 274 -3.7; 302 -2.6; 332 -2.5; 365 -3.2; 402 -3.3; 442 -3.9; 486 -4.5; 535 -3.9; 588 -3.3; 647 -2.8; 712 -2.0; 783 -0.9; 861 0.0; 947 1.0; 1042 -0.0; 1146 0.4; 1261 1.0; 1387 1.0; 1526 0.4; 1678 -0.2; 1846 -0.8; 2031 -1.3; 2234 -2.1; 2457 -2.5; 2703 -2.0; 2973 -0.2; 3270 -0.6; 3597 1.9; 3957 5.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -3.0; 10263 -1.5; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss PRO DJ 100 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss PRO DJ 100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.35 | 6.2 dB  |
| Peaking | 202 Hz  | 1    | -4.5 dB |
| Peaking | 503 Hz  | 2.28 | -3.8 dB |
| Peaking | 2540 Hz | 2.72 | -3.6 dB |
| Peaking | 4930 Hz | 1.82 | 7.3 dB  |
| Peaking | 135 Hz  | 6.52 | -0.6 dB |
| Peaking | 1263 Hz | 2.89 | 1.4 dB  |
| Peaking | 6372 Hz | 6.39 | 2.8 dB  |
| Peaking | 7591 Hz | 4.39 | -1.3 dB |
| Peaking | 9489 Hz | 6.22 | -4.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Koss%20PRO%20DJ%20100/Koss%20PRO%20DJ%20100.png)