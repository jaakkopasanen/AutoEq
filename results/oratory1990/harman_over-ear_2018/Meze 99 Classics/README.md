# Meze 99 Classics

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -2.2; 23 -2.3; 25 -2.5; 28 -2.7; 31 -2.9; 34 -3.1; 37 -3.3; 41 -3.6; 45 -3.8; 49 -4.1; 54 -4.4; 60 -4.8; 66 -5.2; 72 -5.4; 79 -5.7; 87 -5.8; 96 -6.1; 106 -6.4; 116 -7.2; 128 -8.3; 141 -8.4; 155 -9.8; 170 -10.6; 187 -10.8; 206 -10.9; 227 -10.1; 249 -9.3; 274 -7.7; 302 -5.3; 332 -2.7; 365 -1.0; 402 -0.8; 442 -1.5; 486 -2.3; 535 -2.9; 588 -3.1; 647 -3.1; 712 -2.9; 783 -2.4; 861 -1.7; 947 -0.6; 1042 -0.1; 1146 -0.9; 1261 -1.2; 1387 -1.8; 1526 -2.6; 1678 -3.5; 1846 -3.6; 2031 -2.6; 2234 -1.4; 2457 -0.9; 2703 -0.6; 2973 0.4; 3270 2.5; 3597 5.6; 3957 5.5; 4353 -2.5; 4788 -7.1; 5267 -6.8; 5793 -5.8; 6373 -6.3; 7010 -5.9; 7711 -5.7; 8482 -3.0; 9330 0.0; 10263 0.0; 11289 -3.0; 12418 -10.4; 13660 -9.5; 15026 -4.1; 16529 -3.2; 18182 -5.1; 20000 -5.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Meze 99 Classics GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Meze 99 Classics ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 163 Hz   | 0.65 | -10.3 dB |
| Peaking | 3809 Hz  | 2.99 | 17.8 dB  |
| Peaking | 4490 Hz  | 1.19 | -12.7 dB |
| Peaking | 7095 Hz  | 5.13 | -2.1 dB  |
| Peaking | 13225 Hz | 3.33 | -11.3 dB |
| Peaking | 35 Hz    | 1.1  | -2.3 dB  |
| Peaking | 240 Hz   | 3.39 | -2.4 dB  |
| Peaking | 369 Hz   | 3.85 | 4.2 dB   |
| Peaking | 1738 Hz  | 4.18 | -2.9 dB  |
| Peaking | 9951 Hz  | 4.96 | 3.9 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Meze%2099%20Classics/Meze%2099%20Classics.png)