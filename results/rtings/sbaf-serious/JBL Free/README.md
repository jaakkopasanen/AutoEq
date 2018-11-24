# JBL Free

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.6dB
GraphicEQ: 21 -1.8; 23 -1.9; 25 -2.0; 28 -2.1; 31 -2.2; 34 -2.3; 37 -2.4; 41 -2.5; 45 -2.5; 49 -2.6; 54 -2.7; 60 -2.9; 66 -2.9; 72 -2.9; 79 -2.8; 87 -2.9; 96 -3.0; 106 -3.2; 116 -3.3; 128 -3.5; 141 -3.4; 155 -3.1; 170 -3.0; 187 -2.8; 206 -2.8; 227 -2.7; 249 -2.5; 274 -2.2; 302 -1.9; 332 -1.7; 365 -1.4; 402 -1.1; 442 -0.7; 486 -0.2; 535 0.2; 588 0.6; 647 1.2; 712 1.6; 783 1.6; 861 1.1; 947 0.4; 1042 -0.3; 1146 -0.8; 1261 -1.3; 1387 -2.0; 1526 -2.4; 1678 -2.3; 1846 -1.8; 2031 -1.4; 2234 -1.1; 2457 -0.8; 2703 -0.9; 2973 -0.7; 3270 0.4; 3597 1.6; 3957 1.6; 4353 0.9; 4788 2.1; 5267 3.9; 5793 4.4; 6373 1.8; 7010 -1.2; 7711 -0.2; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -1.9; 18182 -1.6; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL Free GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-45**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL Free ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 51 Hz    | 0.39 | -2.5 dB |
| Peaking | 174 Hz   | 0.93 | -2.3 dB |
| Peaking | 1642 Hz  | 2.61 | -2.6 dB |
| Peaking | 5445 Hz  | 4.02 | 4.8 dB  |
| Peaking | 17300 Hz | 3.56 | -2.9 dB |
| Peaking | 328 Hz   | 2.13 | -0.6 dB |
| Peaking | 723 Hz   | 2.55 | 2.2 dB  |
| Peaking | 2937 Hz  | 1.81 | -1.0 dB |
| Peaking | 3655 Hz  | 4.8  | 2.2 dB  |
| Peaking | 7112 Hz  | 9.83 | -2.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/JBL%20Free/JBL%20Free.png)