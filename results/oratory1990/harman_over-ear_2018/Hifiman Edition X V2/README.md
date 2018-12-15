# Hifiman Edition X V2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 5.9; 54 5.5; 60 4.6; 66 3.8; 72 3.1; 79 2.5; 87 2.0; 96 1.3; 106 0.6; 116 -0.1; 128 -1.0; 141 -1.9; 155 -2.7; 170 -3.3; 187 -3.9; 206 -4.6; 227 -5.0; 249 -5.3; 274 -5.4; 302 -4.5; 332 -3.4; 365 -1.8; 402 -3.2; 442 -4.2; 486 -4.2; 535 -4.5; 588 -5.4; 647 -3.8; 712 -0.2; 783 -3.0; 861 -4.0; 947 -3.1; 1042 -0.3; 1146 -1.3; 1261 -1.2; 1387 1.1; 1526 0.8; 1678 1.9; 1846 2.7; 2031 2.8; 2234 1.8; 2457 -0.2; 2703 -1.5; 2973 -2.2; 3270 -2.1; 3597 -1.6; 3957 -1.1; 4353 -0.7; 4788 -0.6; 5267 2.0; 5793 0.6; 6373 -1.2; 7010 -0.7; 7711 -2.8; 8482 -0.9; 9330 0.0; 10263 0.0; 11289 -1.0; 12418 -3.5; 13660 -0.3; 15026 0.0; 16529 0.0; 18182 -0.3; 20000 -11.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Hifiman Edition X V2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Hifiman Edition X V2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 33 Hz    | 0.45 | 6.6 dB   |
| Peaking | 224 Hz   | 0.86 | -5.8 dB  |
| Peaking | 566 Hz   | 3.67 | -4.2 dB  |
| Peaking | 879 Hz   | 6.16 | -3.6 dB  |
| Peaking | 1870 Hz  | 4.41 | 3.5 dB   |
| Peaking | 2192 Hz  | 4.8  | 1.7 dB   |
| Peaking | 3044 Hz  | 2.37 | -2.6 dB  |
| Peaking | 10969 Hz | 5.92 | 1.2 dB   |
| Peaking | 12201 Hz | 4.7  | -3.9 dB  |
| Peaking | 19839 Hz | 4.21 | -11.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Hifiman%20Edition%20X%20V2/Hifiman%20Edition%20X%20V2.png)