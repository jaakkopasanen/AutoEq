# Periodic Audio Be

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.8dB
GraphicEQ: 21 -8.4; 23 -8.4; 25 -8.4; 28 -8.3; 31 -8.2; 34 -8.1; 37 -8.1; 41 -8.0; 45 -8.0; 49 -8.0; 54 -8.0; 60 -7.9; 66 -7.8; 72 -7.8; 79 -7.8; 87 -7.7; 96 -7.7; 106 -7.7; 116 -7.6; 128 -7.5; 141 -7.3; 155 -6.9; 170 -6.6; 187 -6.1; 206 -5.5; 227 -4.8; 249 -4.5; 274 -5.4; 302 -4.7; 332 -3.8; 365 -3.2; 402 -2.8; 442 -2.4; 486 -1.9; 535 -1.3; 588 -0.8; 647 -0.4; 712 0.0; 783 0.4; 861 0.5; 947 0.3; 1042 -0.2; 1146 -0.9; 1261 -1.4; 1387 -1.4; 1526 -1.1; 1678 -1.0; 1846 -1.3; 2031 -1.0; 2234 -0.4; 2457 0.4; 2703 1.4; 2973 2.6; 3270 3.6; 3597 4.3; 3957 4.7; 4353 4.4; 4788 3.5; 5267 1.7; 5793 -2.0; 6373 -3.8; 7010 0.9; 7711 0.3; 8482 0.0; 9330 -2.4; 10263 -1.2; 11289 0.0; 12418 -0.0; 13660 -7.4; 15026 -17.5; 16529 -23.9; 18182 -24.7; 20000 -19.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Periodic Audio Be GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-47**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Periodic Audio Be ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 21 Hz    | 0.26 | -8.0 dB  |
| Peaking | 136 Hz   | 0.63 | -4.8 dB  |
| Peaking | 305 Hz   | 2.09 | -2.0 dB  |
| Peaking | 4017 Hz  | 1.94 | 5.8 dB   |
| Peaking | 17899 Hz | 1.43 | -28.5 dB |
| Peaking | 1732 Hz  | 2.13 | -1.6 dB  |
| Peaking | 6210 Hz  | 5.47 | -7.3 dB  |
| Peaking | 6957 Hz  | 2.04 | 3.7 dB   |
| Peaking | 12448 Hz | 2.29 | 9.5 dB   |
| Peaking | 15447 Hz | 1.98 | -9.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Periodic%20Audio%20Be/Periodic%20Audio%20Be.png)