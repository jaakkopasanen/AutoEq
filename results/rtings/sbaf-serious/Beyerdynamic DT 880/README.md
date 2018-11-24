# Beyerdynamic DT 880

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 5.9; 28 5.7; 31 5.4; 34 5.1; 37 4.9; 41 4.7; 45 4.5; 49 4.3; 54 4.1; 60 4.0; 66 3.8; 72 3.6; 79 3.3; 87 2.9; 96 2.5; 106 2.1; 116 1.6; 128 1.2; 141 0.9; 155 0.6; 170 0.4; 187 0.3; 206 0.2; 227 0.2; 249 0.3; 274 0.4; 302 0.4; 332 0.5; 365 0.6; 402 0.4; 442 0.2; 486 0.5; 535 0.6; 588 0.4; 647 0.5; 712 0.4; 783 -0.0; 861 -0.1; 947 -0.1; 1042 0.2; 1146 0.7; 1261 0.8; 1387 0.5; 1526 -0.1; 1678 -1.0; 1846 -1.7; 2031 -1.9; 2234 -1.9; 2457 -1.4; 2703 -1.4; 2973 -0.7; 3270 0.9; 3597 2.8; 3957 2.9; 4353 1.6; 4788 2.0; 5267 2.1; 5793 -0.9; 6373 -1.8; 7010 -0.3; 7711 -3.8; 8482 -8.9; 9330 -9.2; 10263 -4.9; 11289 -0.5; 12418 0.0; 13660 0.0; 15026 -0.1; 16529 -1.4; 18182 -3.3; 20000 -4.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 880 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 880 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 22 Hz    | 0.47 | 5.9 dB   |
| Peaking | 73 Hz    | 1.27 | 1.7 dB   |
| Peaking | 2521 Hz  | 1.7  | -3.1 dB  |
| Peaking | 3861 Hz  | 1.63 | 3.9 dB   |
| Peaking | 8964 Hz  | 3.54 | -10.9 dB |
| Peaking | 1535 Hz  | 1.34 | 1.5 dB   |
| Peaking | 1798 Hz  | 2.92 | -2.1 dB  |
| Peaking | 4336 Hz  | 8.88 | -0.7 dB  |
| Peaking | 12996 Hz | 2.04 | 1.5 dB   |
| Peaking | 19548 Hz | 1.15 | -4.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Beyerdynamic%20DT%20880/Beyerdynamic%20DT%20880.png)