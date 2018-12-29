# Mee Audio Pinnacle PX

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.3dB
GraphicEQ: 21 -0.6; 23 -0.9; 25 -1.2; 28 -1.6; 31 -1.9; 34 -2.1; 37 -2.4; 41 -2.7; 45 -2.9; 49 -3.2; 54 -3.5; 60 -3.8; 66 -4.1; 72 -4.5; 79 -4.8; 87 -5.3; 96 -5.5; 106 -5.8; 116 -6.1; 128 -6.3; 141 -6.3; 155 -6.3; 170 -7.5; 187 -7.7; 206 -7.4; 227 -7.1; 249 -6.8; 274 -6.3; 302 -5.9; 332 -5.3; 365 -5.1; 402 -4.7; 442 -4.2; 486 -3.6; 535 -2.9; 588 -2.3; 647 -1.8; 712 -1.2; 783 -0.5; 861 -0.1; 947 0.0; 1042 -0.0; 1146 -0.2; 1261 -0.3; 1387 0.3; 1526 0.9; 1678 1.7; 1846 1.8; 2031 1.9; 2234 1.6; 2457 0.8; 2703 -0.4; 2973 -1.0; 3270 -0.5; 3597 0.1; 3957 -0.3; 4353 -1.9; 4788 -3.6; 5267 -4.0; 5793 -0.4; 6373 2.5; 7010 2.4; 7711 -0.3; 8482 -2.2; 9330 -0.9; 10263 -0.4; 11289 -3.2; 12418 -8.5; 13660 -17.5; 15026 -27.3; 16529 -28.1; 18182 -19.7; 20000 -9.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Mee Audio Pinnacle PX GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-32**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Mee Audio Pinnacle PX ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 104 Hz   | 0.42 | -4.2 dB  |
| Peaking | 248 Hz   | 0.71 | -4.6 dB  |
| Peaking | 4946 Hz  | 3.16 | -6.5 dB  |
| Peaking | 8739 Hz  | 0.41 | 16.7 dB  |
| Peaking | 15736 Hz | 0.75 | -40.4 dB |
| Peaking | 2005 Hz  | 2.06 | 1.7 dB   |
| Peaking | 2917 Hz  | 2.93 | -2.4 dB  |
| Peaking | 8563 Hz  | 3.63 | -7.0 dB  |
| Peaking | 9878 Hz  | 1.17 | 4.5 dB   |
| Peaking | 14106 Hz | 3.79 | -4.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Mee%20Audio%20Pinnacle%20PX/Mee%20Audio%20Pinnacle%20PX.png)