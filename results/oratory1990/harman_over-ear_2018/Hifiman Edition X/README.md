# Hifiman Edition X

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 5.9; 79 5.6; 87 5.2; 96 4.6; 106 4.0; 116 3.3; 128 2.8; 141 2.0; 155 1.2; 170 0.6; 187 0.1; 206 -0.3; 227 -0.5; 249 -0.1; 274 -0.0; 302 -0.1; 332 -0.0; 365 0.5; 402 1.6; 442 1.5; 486 1.2; 535 1.0; 588 1.0; 647 0.9; 712 0.5; 783 -0.5; 861 2.2; 947 0.9; 1042 -0.3; 1146 -0.4; 1261 3.2; 1387 4.3; 1526 3.8; 1678 4.6; 1846 5.0; 2031 4.8; 2234 4.0; 2457 2.5; 2703 1.5; 2973 0.8; 3270 1.1; 3597 1.7; 3957 2.3; 4353 2.8; 4788 3.2; 5267 3.7; 5793 1.3; 6373 0.0; 7010 2.2; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -5.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Hifiman Edition X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Hifiman Edition X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 42 Hz   |  1.84 | -4.1 dB |
| Peaking | 42 Hz   |  0.63 | 9.8 dB  |
| Peaking | 439 Hz  |  5.23 | 1.4 dB  |
| Peaking | 1798 Hz |  1.76 | 5.3 dB  |
| Peaking | 4875 Hz |  2.87 | 3.4 dB  |
| Peaking | 98 Hz   |  2.2  | 1.0 dB  |
| Peaking | 209 Hz  |  1.99 | -1.6 dB |
| Peaking | 1133 Hz |  6.71 | -2.5 dB |
| Peaking | 1316 Hz | 10.02 | 3.1 dB  |
| Peaking | 2921 Hz |  9.06 | -0.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Hifiman%20Edition%20X/Hifiman%20Edition%20X.png)