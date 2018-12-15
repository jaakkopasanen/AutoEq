# JBL Endurance Sprint

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.4dB
GraphicEQ: 21 -2.5; 23 -2.5; 25 -2.5; 28 -2.5; 31 -2.6; 34 -2.6; 37 -2.7; 41 -2.7; 45 -2.6; 49 -2.5; 54 -2.5; 60 -2.6; 66 -2.6; 72 -2.6; 79 -2.5; 87 -2.4; 96 -2.2; 106 -2.0; 116 -1.8; 128 -1.7; 141 -1.5; 155 -1.1; 170 -0.5; 187 0.1; 206 0.5; 227 0.9; 249 1.1; 274 1.1; 302 1.1; 332 0.9; 365 0.7; 402 0.5; 442 0.5; 486 0.5; 535 0.6; 588 0.9; 647 1.2; 712 1.2; 783 1.3; 861 1.0; 947 0.4; 1042 -0.3; 1146 -0.9; 1261 -1.4; 1387 -1.6; 1526 -1.2; 1678 -0.8; 1846 -1.1; 2031 -1.3; 2234 -0.7; 2457 -0.1; 2703 -0.3; 2973 -1.2; 3270 -2.0; 3597 -2.3; 3957 -3.0; 4353 -3.7; 4788 -4.2; 5267 -5.7; 5793 -7.3; 6373 -6.3; 7010 -4.9; 7711 -5.5; 8482 -5.6; 9330 -3.1; 10263 -0.3; 11289 0.0; 12418 -2.2; 13660 -8.4; 15026 -15.9; 16529 -18.9; 18182 -14.8; 20000 -5.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL Endurance Sprint GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-13**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL Endurance Sprint ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 55 Hz    | 0.31 | -3.1 dB  |
| Peaking | 332 Hz   | 0.38 | 1.7 dB   |
| Peaking | 1367 Hz  | 2.14 | -1.9 dB  |
| Peaking | 5780 Hz  | 1.76 | -6.3 dB  |
| Peaking | 16791 Hz | 1.58 | -20.9 dB |
| Peaking | 450 Hz   | 4.64 | -0.8 dB  |
| Peaking | 8440 Hz  | 3.67 | -3.9 dB  |
| Peaking | 11321 Hz | 1.8  | 5.6 dB   |
| Peaking | 14792 Hz | 3.88 | -5.8 dB  |
| Peaking | 18823 Hz | 4.24 | -3.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/JBL%20Endurance%20Sprint/JBL%20Endurance%20Sprint.png)