# Hifiman Edition X V2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.0dB
GraphicEQ: 21 0.0; 23 0.6; 25 0.5; 28 0.5; 31 0.5; 34 0.4; 37 0.4; 41 0.3; 45 0.4; 49 0.5; 54 0.3; 60 -0.4; 66 -0.8; 72 -1.3; 79 -1.6; 87 -1.8; 96 -2.0; 106 -2.2; 116 -2.4; 128 -2.9; 141 -3.3; 155 -3.7; 170 -3.9; 187 -4.2; 206 -4.7; 227 -5.0; 249 -5.3; 274 -5.4; 302 -4.5; 332 -3.4; 365 -1.8; 402 -3.2; 442 -4.2; 486 -4.2; 535 -4.5; 588 -5.4; 647 -3.8; 712 -0.2; 783 -3.0; 861 -4.0; 947 -3.1; 1042 -0.3; 1146 -1.3; 1261 -1.2; 1387 1.1; 1526 0.8; 1678 1.9; 1846 2.7; 2031 2.8; 2234 1.8; 2457 -0.2; 2703 -1.5; 2973 -2.2; 3270 -2.1; 3597 -1.6; 3957 -1.1; 4353 -0.7; 4788 -0.6; 5267 2.0; 5793 0.6; 6373 -1.2; 7010 -0.7; 7711 -2.8; 8482 -0.9; 9330 0.0; 10263 0.0; 11289 -1.0; 12418 -3.5; 13660 -0.3; 15026 0.0; 16529 0.0; 18182 -0.3; 20000 -11.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Hifiman Edition X V2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-30**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Hifiman Edition X V2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.1dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 224 Hz   |  0.74 | -4.9 dB  |
| Peaking | 570 Hz   |  4.04 | -4.1 dB  |
| Peaking | 881 Hz   |  6.1  | -3.6 dB  |
| Peaking | 1982 Hz  |  2.4  | 4.0 dB   |
| Peaking | 2973 Hz  |  1.93 | -3.0 dB  |
| Peaking | 454 Hz   | 11.63 | -1.4 dB  |
| Peaking | 5420 Hz  | 10.9  | 3.4 dB   |
| Peaking | 7804 Hz  |  8.25 | -2.7 dB  |
| Peaking | 18124 Hz |  1.26 | 8.5 dB   |
| Peaking | 20464 Hz |  0.73 | -15.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Hifiman%20Edition%20X%20V2/Hifiman%20Edition%20X%20V2.png)