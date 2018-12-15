# Mee Audio Planamic IEM

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 4.2; 25 4.1; 28 3.9; 31 3.7; 34 3.5; 37 3.3; 41 2.9; 45 2.5; 49 2.1; 54 1.5; 60 0.8; 66 0.1; 72 -0.6; 79 -1.4; 87 -2.1; 96 -2.9; 106 -3.5; 116 -4.1; 128 -4.6; 141 -5.3; 155 -5.8; 170 -6.1; 187 -6.2; 206 -6.5; 227 -6.9; 249 -6.8; 274 -6.3; 302 -5.7; 332 -4.9; 365 -4.0; 402 -3.3; 442 -2.9; 486 -2.5; 535 -1.9; 588 -1.3; 647 -0.8; 712 -0.3; 783 0.1; 861 0.4; 947 0.2; 1042 -0.2; 1146 -0.5; 1261 -0.9; 1387 -1.1; 1526 -1.3; 1678 -1.7; 1846 -1.9; 2031 -1.9; 2234 -2.1; 2457 -2.9; 2703 -3.1; 2973 -3.2; 3270 -3.6; 3597 -4.6; 3957 -6.0; 4353 -3.4; 4788 1.8; 5267 5.7; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 -0.0; 13660 -7.2; 15026 -14.7; 16529 -14.1; 18182 -8.3; 20000 -1.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Mee Audio Planamic IEM GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Mee Audio Planamic IEM ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 27 Hz    | 0.69 | 4.5 dB   |
| Peaking | 199 Hz   | 0.72 | -7.1 dB  |
| Peaking | 4221 Hz  | 1.15 | -18.8 dB |
| Peaking | 5160 Hz  | 1.15 | 19.7 dB  |
| Peaking | 16004 Hz | 1.76 | -17.2 dB |
| Peaking | 296 Hz   | 3.79 | -0.8 dB  |
| Peaking | 830 Hz   | 2.7  | 1.6 dB   |
| Peaking | 7977 Hz  | 5.24 | -2.2 dB  |
| Peaking | 12588 Hz | 3.18 | 4.5 dB   |
| Peaking | 14456 Hz | 4.94 | -4.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Mee%20Audio%20Planamic%20IEM/Mee%20Audio%20Planamic%20IEM.png)