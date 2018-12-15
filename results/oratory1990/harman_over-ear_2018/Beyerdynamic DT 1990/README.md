# Beyerdynamic DT 1990

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.2dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 5.6; 72 5.1; 79 4.4; 87 3.7; 96 2.9; 106 2.0; 116 1.0; 128 0.1; 141 -0.8; 155 -1.6; 170 -2.2; 187 -2.6; 206 -3.0; 227 -3.1; 249 -3.1; 274 -2.9; 302 -2.7; 332 -2.4; 365 -2.1; 402 -1.8; 442 -1.6; 486 -1.4; 535 -1.1; 588 -0.7; 647 -0.5; 712 -0.3; 783 -0.1; 861 0.1; 947 0.1; 1042 -0.0; 1146 -0.3; 1261 -0.5; 1387 -0.6; 1526 -0.7; 1678 -0.6; 1846 -0.3; 2031 0.1; 2234 0.2; 2457 -0.3; 2703 -0.9; 2973 -0.0; 3270 1.3; 3597 2.1; 3957 3.7; 4353 6.0; 4788 1.4; 5267 -1.8; 5793 -2.1; 6373 -1.4; 7010 -6.9; 7711 -10.3; 8482 -8.3; 9330 -3.3; 10263 -1.9; 11289 -3.9; 12418 -6.3; 13660 -8.6; 15026 -10.2; 16529 -9.6; 18182 -7.2; 20000 -5.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 1990 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 1990 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 49 Hz    | 0.27 | 7.2 dB   |
| Peaking | 191 Hz   | 0.67 | -6.5 dB  |
| Peaking | 4240 Hz  | 5.12 | 7.1 dB   |
| Peaking | 7747 Hz  | 4.43 | -9.8 dB  |
| Peaking | 16069 Hz | 0.9  | -10.5 dB |
| Peaking | 1548 Hz  | 4.8  | -0.6 dB  |
| Peaking | 3446 Hz  | 9.19 | 1.1 dB   |
| Peaking | 5340 Hz  | 9.57 | -1.9 dB  |
| Peaking | 10235 Hz | 6.22 | 2.8 dB   |
| Peaking | 13615 Hz | 4.01 | -1.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Beyerdynamic%20DT%201990/Beyerdynamic%20DT%201990.png)