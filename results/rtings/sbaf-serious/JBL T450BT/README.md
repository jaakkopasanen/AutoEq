# JBL T450BT

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.2; 25 1.7; 28 0.9; 31 0.2; 34 -0.3; 37 -0.8; 41 -1.3; 45 -1.7; 49 -1.9; 54 -2.2; 60 -2.6; 66 -3.1; 72 -3.4; 79 -3.6; 87 -3.9; 96 -4.0; 106 -4.3; 116 -4.5; 128 -4.5; 141 -4.4; 155 -4.3; 170 -4.2; 187 -3.9; 206 -3.5; 227 -2.8; 249 -1.9; 274 -1.0; 302 0.1; 332 0.1; 365 0.8; 402 1.7; 442 1.7; 486 1.5; 535 1.3; 588 1.0; 647 0.9; 712 0.6; 783 0.3; 861 -0.0; 947 -0.1; 1042 0.2; 1146 0.6; 1261 0.8; 1387 0.3; 1526 0.1; 1678 0.3; 1846 1.1; 2031 1.7; 2234 2.8; 2457 2.7; 2703 2.4; 2973 2.0; 3270 2.3; 3597 3.7; 3957 4.3; 4353 4.2; 4788 5.8; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 -0.7; 8482 -4.6; 9330 -6.5; 10263 -3.4; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL T450BT GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL T450BT ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 2.4  | 3.2 dB  |
| Peaking | 121 Hz  | 0.71 | -5.4 dB |
| Peaking | 1419 Hz | 0.08 | 1.1 dB  |
| Peaking | 5670 Hz | 1.24 | 6.3 dB  |
| Peaking | 8997 Hz | 2.72 | -9.7 dB |
| Peaking | 209 Hz  | 3.16 | -1.3 dB |
| Peaking | 422 Hz  | 1.81 | 1.7 dB  |
| Peaking | 904 Hz  | 2.71 | -1.2 dB |
| Peaking | 1586 Hz | 3.36 | -1.2 dB |
| Peaking | 2309 Hz | 5.42 | 1.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/JBL%20T450BT/JBL%20T450BT.png)