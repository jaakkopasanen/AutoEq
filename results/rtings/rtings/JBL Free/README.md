# JBL Free

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.6dB
GraphicEQ: 21 -2.2; 23 -2.3; 25 -2.3; 28 -2.3; 31 -2.3; 34 -2.3; 37 -2.3; 41 -2.3; 45 -2.3; 49 -2.2; 54 -2.3; 60 -2.6; 66 -2.8; 72 -2.9; 79 -3.0; 87 -3.2; 96 -3.4; 106 -3.6; 116 -3.8; 128 -4.0; 141 -4.0; 155 -3.7; 170 -3.6; 187 -3.4; 206 -3.3; 227 -3.2; 249 -3.1; 274 -2.9; 302 -2.7; 332 -2.6; 365 -2.4; 402 -2.2; 442 -1.9; 486 -1.4; 535 -1.0; 588 -0.5; 647 0.2; 712 0.8; 783 1.1; 861 0.9; 947 0.4; 1042 -0.3; 1146 -1.0; 1261 -1.6; 1387 -1.9; 1526 -2.0; 1678 -2.0; 1846 -1.9; 2031 -1.9; 2234 -1.5; 2457 -1.2; 2703 -1.5; 2973 -1.8; 3270 -1.5; 3597 -0.5; 3957 0.4; 4353 0.8; 4788 2.3; 5267 3.4; 5793 3.0; 6373 -0.8; 7010 -3.7; 7711 -1.3; 8482 0.0; 9330 -1.2; 10263 -2.9; 11289 -3.1; 12418 -3.0; 13660 -1.5; 15026 -1.8; 16529 -5.3; 18182 -4.8; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL Free GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-35**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL Free ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 117 Hz   | 0.38 | -3.8 dB |
| Peaking | 5171 Hz  | 2.42 | 6.6 dB  |
| Peaking | 6029 Hz  | 0.34 | -2.9 dB |
| Peaking | 17342 Hz | 2.54 | -5.7 dB |
| Peaking | 24000 Hz | 1.58 | -3.7 dB |
| Peaking | 21 Hz    | 1.91 | -1.6 dB |
| Peaking | 782 Hz   | 3.66 | 2.3 dB  |
| Peaking | 7057 Hz  | 5.64 | -4.7 dB |
| Peaking | 8527 Hz  | 1.74 | 3.8 dB  |
| Peaking | 10405 Hz | 2.39 | -2.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/JBL%20Free/JBL%20Free.png)