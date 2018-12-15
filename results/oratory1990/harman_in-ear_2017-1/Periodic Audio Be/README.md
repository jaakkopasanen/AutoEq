# Periodic Audio Be

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.8dB
GraphicEQ: 21 0.0; 23 1.2; 25 1.3; 28 1.4; 31 1.4; 34 1.4; 37 1.3; 41 1.1; 45 0.9; 49 0.6; 54 0.2; 60 -0.3; 66 -0.7; 72 -1.2; 79 -1.7; 87 -2.3; 96 -2.8; 106 -3.4; 116 -3.9; 128 -4.3; 141 -4.7; 155 -4.9; 170 -5.0; 187 -5.1; 206 -5.0; 227 -4.6; 249 -4.5; 274 -5.4; 302 -4.7; 332 -3.8; 365 -3.2; 402 -2.8; 442 -2.4; 486 -1.9; 535 -1.3; 588 -0.8; 647 -0.4; 712 0.0; 783 0.4; 861 0.5; 947 0.3; 1042 -0.2; 1146 -0.9; 1261 -1.4; 1387 -1.4; 1526 -1.1; 1678 -1.0; 1846 -1.3; 2031 -1.0; 2234 -0.4; 2457 0.4; 2703 1.4; 2973 2.6; 3270 3.6; 3597 4.3; 3957 4.7; 4353 4.4; 4788 3.5; 5267 1.7; 5793 -2.0; 6373 -3.8; 7010 0.9; 7711 0.3; 8482 0.0; 9330 -2.4; 10263 -1.2; 11289 0.0; 12418 -0.0; 13660 -7.4; 15026 -17.5; 16529 -23.9; 18182 -24.7; 20000 -19.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Periodic Audio Be GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-47**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Periodic Audio Be ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 203 Hz   | 0.66 | -5.4 dB  |
| Peaking | 6256 Hz  | 5.88 | -8.1 dB  |
| Peaking | 9346 Hz  | 3.19 | -10.3 dB |
| Peaking | 9754 Hz  | 0.55 | 23.0 dB  |
| Peaking | 17258 Hz | 0.52 | -36.1 dB |
| Peaking | 33 Hz    | 1.24 | 2.0 dB   |
| Peaking | 1845 Hz  | 1.66 | -2.5 dB  |
| Peaking | 3793 Hz  | 2.34 | 3.3 dB   |
| Peaking | 12791 Hz | 3.38 | 9.0 dB   |
| Peaking | 13820 Hz | 1.35 | -5.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Periodic%20Audio%20Be/Periodic%20Audio%20Be.png)