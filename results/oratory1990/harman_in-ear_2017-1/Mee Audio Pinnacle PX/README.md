# Mee Audio Pinnacle PX

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 5.9; 49 5.4; 54 4.6; 60 3.8; 66 3.0; 72 2.1; 79 1.2; 87 0.2; 96 -0.6; 106 -1.5; 116 -2.4; 128 -3.1; 141 -3.7; 155 -4.2; 170 -6.0; 187 -6.7; 206 -6.8; 227 -6.8; 249 -6.7; 274 -6.4; 302 -5.9; 332 -5.3; 365 -5.1; 402 -4.7; 442 -4.2; 486 -3.6; 535 -2.9; 588 -2.3; 647 -1.8; 712 -1.2; 783 -0.5; 861 -0.1; 947 0.0; 1042 -0.0; 1146 -0.2; 1261 -0.3; 1387 0.3; 1526 0.9; 1678 1.7; 1846 1.8; 2031 1.9; 2234 1.6; 2457 0.8; 2703 -0.4; 2973 -1.0; 3270 -0.5; 3597 0.1; 3957 -0.3; 4353 -1.9; 4788 -3.6; 5267 -4.0; 5793 -0.4; 6373 2.5; 7010 2.4; 7711 -0.3; 8482 -2.2; 9330 -0.9; 10263 -0.4; 11289 -3.2; 12418 -8.5; 13660 -17.5; 15026 -27.3; 16529 -28.1; 18182 -19.7; 20000 -9.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Mee Audio Pinnacle PX GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Mee Audio Pinnacle PX ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 33 Hz    | 0.51 | 6.9 dB   |
| Peaking | 221 Hz   | 0.66 | -7.6 dB  |
| Peaking | 4940 Hz  | 3.08 | -6.5 dB  |
| Peaking | 8715 Hz  | 0.41 | 16.6 dB  |
| Peaking | 15735 Hz | 0.75 | -40.3 dB |
| Peaking | 2001 Hz  | 1.97 | 1.7 dB   |
| Peaking | 2911 Hz  | 3.01 | -2.5 dB  |
| Peaking | 8542 Hz  | 3.64 | -6.9 dB  |
| Peaking | 9906 Hz  | 1.17 | 4.6 dB   |
| Peaking | 14241 Hz | 3.69 | -4.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Mee%20Audio%20Pinnacle%20PX/Mee%20Audio%20Pinnacle%20PX.png)