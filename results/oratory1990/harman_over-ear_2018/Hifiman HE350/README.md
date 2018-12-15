# Hifiman HE350

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 5.9; 87 5.3; 96 4.2; 106 3.3; 116 2.4; 128 1.3; 141 0.3; 155 -0.3; 170 -0.8; 187 -1.1; 206 -1.3; 227 -1.4; 249 -1.2; 274 -0.8; 302 -0.3; 332 0.1; 365 0.5; 402 0.7; 442 0.7; 486 0.3; 535 0.3; 588 0.3; 647 0.5; 712 0.7; 783 0.4; 861 0.1; 947 -0.0; 1042 0.0; 1146 0.3; 1261 0.8; 1387 1.4; 1526 2.0; 1678 2.6; 1846 3.6; 2031 4.6; 2234 4.3; 2457 2.9; 2703 2.1; 2973 2.1; 3270 1.9; 3597 0.8; 3957 -1.2; 4353 -3.0; 4788 -4.4; 5267 -5.4; 5793 -5.4; 6373 -3.7; 7010 -0.5; 7711 0.3; 8482 -0.0; 9330 -2.6; 10263 -4.9; 11289 -5.9; 12418 -6.9; 13660 -7.4; 15026 -5.3; 16529 -0.8; 18182 0.0; 20000 -0.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Hifiman HE350 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Hifiman HE350 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 55 Hz    | 0.24 | 7.0 dB  |
| Peaking | 180 Hz   | 0.92 | -5.9 dB |
| Peaking | 2158 Hz  | 1.66 | 4.6 dB  |
| Peaking | 5268 Hz  | 3.02 | -6.1 dB |
| Peaking | 12989 Hz | 1.72 | -8.0 dB |
| Peaking | 3327 Hz  | 6.28 | 1.5 dB  |
| Peaking | 7833 Hz  | 2.88 | 4.9 dB  |
| Peaking | 8103 Hz  | 1.02 | -2.5 dB |
| Peaking | 17419 Hz | 3.09 | 1.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Hifiman%20HE350/Hifiman%20HE350.png)