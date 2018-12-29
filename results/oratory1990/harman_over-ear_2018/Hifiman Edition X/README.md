# Hifiman Edition X

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.8; 25 5.4; 28 4.6; 31 4.0; 34 3.6; 37 3.4; 41 3.3; 45 3.2; 49 3.1; 54 2.9; 60 2.6; 66 2.0; 72 1.6; 79 1.4; 87 1.4; 96 1.3; 106 1.1; 116 1.0; 128 0.9; 141 0.6; 155 0.2; 170 -0.0; 187 -0.2; 206 -0.4; 227 -0.5; 249 -0.1; 274 -0.0; 302 -0.1; 332 -0.0; 365 0.5; 402 1.6; 442 1.5; 486 1.2; 535 1.0; 588 1.0; 647 0.9; 712 0.5; 783 -0.5; 861 2.2; 947 0.9; 1042 -0.3; 1146 -0.4; 1261 3.2; 1387 4.3; 1526 3.8; 1678 4.6; 1846 5.0; 2031 4.8; 2234 4.0; 2457 2.5; 2703 1.5; 2973 0.8; 3270 1.1; 3597 1.7; 3957 2.3; 4353 2.8; 4788 3.2; 5267 3.7; 5793 1.3; 6373 0.0; 7010 2.2; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -5.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Hifiman Edition X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Hifiman Edition X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 1.09 | 5.7 dB  |
| Peaking | 52 Hz   | 0.99 | 2.0 dB  |
| Peaking | 439 Hz  | 3.76 | 1.6 dB  |
| Peaking | 1796 Hz | 1.74 | 5.3 dB  |
| Peaking | 4877 Hz | 2.88 | 3.4 dB  |
| Peaking | 216 Hz  | 3.25 | -0.8 dB |
| Peaking | 1144 Hz | 6.23 | -2.6 dB |
| Peaking | 1330 Hz | 8.9  | 3.1 dB  |
| Peaking | 2957 Hz | 6.71 | -0.9 dB |
| Peaking | 3808 Hz | 5.53 | 0.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Hifiman%20Edition%20X/Hifiman%20Edition%20X.png)