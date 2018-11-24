# JBL Endurance Sprint

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.3dB
GraphicEQ: 21 -2.1; 23 -2.2; 25 -2.2; 28 -2.4; 31 -2.5; 34 -2.7; 37 -2.8; 41 -2.9; 45 -2.9; 49 -2.9; 54 -2.8; 60 -2.9; 66 -2.8; 72 -2.6; 79 -2.3; 87 -2.0; 96 -1.8; 106 -1.5; 116 -1.2; 128 -1.2; 141 -0.9; 155 -0.5; 170 0.1; 187 0.6; 206 1.0; 227 1.3; 249 1.6; 274 1.8; 302 1.9; 332 1.8; 365 1.7; 402 1.6; 442 1.6; 486 1.7; 535 1.8; 588 2.0; 647 2.2; 712 2.1; 783 1.7; 861 1.1; 947 0.4; 1042 -0.2; 1146 -0.7; 1261 -1.1; 1387 -1.7; 1526 -1.5; 1678 -1.1; 1846 -1.0; 2031 -0.8; 2234 -0.3; 2457 0.4; 2703 0.5; 2973 0.3; 3270 0.5; 3597 0.8; 3957 -0.5; 4353 -2.4; 4788 -2.6; 5267 -2.7; 5793 -3.4; 6373 -2.5; 7010 -1.5; 7711 -3.0; 8482 -4.5; 9330 -3.0; 10263 -0.0; 11289 0.0; 12418 0.0; 13660 -1.7; 15026 -10.0; 16529 -12.5; 18182 -7.2; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL Endurance Sprint GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-23**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL Endurance Sprint ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 35 Hz    | 0.96 | -2.7 dB  |
| Peaking | 71 Hz    | 1.67 | -2.1 dB  |
| Peaking | 6202 Hz  | 1.45 | -2.9 dB  |
| Peaking | 16464 Hz | 2.3  | -14.1 dB |
| Peaking | 24000 Hz | 1.5  | -3.0 dB  |
| Peaking | 918 Hz   | 0.38 | 3.4 dB   |
| Peaking | 1372 Hz  | 1.1  | -4.6 dB  |
| Peaking | 8632 Hz  | 5.91 | -3.9 dB  |
| Peaking | 12954 Hz | 1.72 | 3.6 dB   |
| Peaking | 14923 Hz | 4.48 | -4.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/JBL%20Endurance%20Sprint/JBL%20Endurance%20Sprint.png)