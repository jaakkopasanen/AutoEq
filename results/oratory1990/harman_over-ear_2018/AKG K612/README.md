# AKG K612

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 5.9; 31 5.7; 34 5.3; 37 4.9; 41 4.5; 45 4.3; 49 4.4; 54 4.8; 60 4.9; 66 4.1; 72 3.3; 79 2.8; 87 2.1; 96 1.5; 106 1.0; 116 0.5; 128 0.1; 141 -0.3; 155 -0.4; 170 -0.7; 187 -0.9; 206 -1.0; 227 -1.1; 249 -1.0; 274 -0.9; 302 -0.6; 332 -0.3; 365 -0.2; 402 -0.1; 442 0.1; 486 0.3; 535 0.5; 588 0.7; 647 1.1; 712 1.3; 783 0.7; 861 0.1; 947 0.0; 1042 -0.0; 1146 0.2; 1261 0.1; 1387 -0.6; 1526 -1.7; 1678 -2.7; 1846 -3.4; 2031 -3.5; 2234 -3.1; 2457 -3.8; 2703 -3.1; 2973 -3.0; 3270 -1.4; 3597 -1.4; 3957 -0.4; 4353 0.4; 4788 -0.6; 5267 -1.1; 5793 -2.9; 6373 -2.8; 7010 -2.7; 7711 -2.8; 8482 -0.2; 9330 0.0; 10263 0.0; 11289 -0.0; 12418 -2.5; 13660 -0.9; 15026 0.0; 16529 -2.9; 18182 -7.1; 20000 -5.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K612 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K612 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 26 Hz    | 0.97 | 6.2 dB  |
| Peaking | 59 Hz    | 2.04 | 3.6 dB  |
| Peaking | 2256 Hz  | 1.74 | -3.9 dB |
| Peaking | 6590 Hz  | 2.94 | -3.0 dB |
| Peaking | 18766 Hz | 1.7  | -8.0 dB |
| Peaking | 219 Hz   | 1.43 | -1.4 dB |
| Peaking | 683 Hz   | 1.99 | 1.4 dB  |
| Peaking | 4130 Hz  | 1.38 | -1.0 dB |
| Peaking | 4331 Hz  | 4.23 | 2.3 dB  |
| Peaking | 15952 Hz | 4.54 | 1.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/AKG%20K612/AKG%20K612.png)