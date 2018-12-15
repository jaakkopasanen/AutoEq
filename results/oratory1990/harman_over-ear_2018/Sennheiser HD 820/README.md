# Sennheiser HD 820

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 4.0; 25 3.8; 28 3.5; 31 3.2; 34 3.0; 37 2.7; 41 2.3; 45 2.0; 49 1.8; 54 1.6; 60 1.6; 66 2.3; 72 4.2; 79 5.8; 87 3.8; 96 0.6; 106 -1.5; 116 -2.8; 128 -3.5; 141 -3.8; 155 -4.3; 170 -4.1; 187 -3.2; 206 -1.2; 227 1.8; 249 5.5; 274 6.0; 302 6.0; 332 6.0; 365 5.4; 402 4.1; 442 3.1; 486 2.6; 535 2.0; 588 1.7; 647 1.5; 712 1.3; 783 1.0; 861 0.4; 947 0.1; 1042 0.1; 1146 0.5; 1261 1.4; 1387 2.3; 1526 3.0; 1678 3.5; 1846 3.7; 2031 3.7; 2234 3.6; 2457 2.7; 2703 1.9; 2973 2.4; 3270 4.6; 3597 6.0; 3957 6.0; 4353 5.8; 4788 1.4; 5267 0.7; 5793 3.2; 6373 4.0; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -4.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 820 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 820 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 20 Hz   | 0.55 | 4.3 dB   |
| Peaking | 80 Hz   | 3.53 | 7.1 dB   |
| Peaking | 175 Hz  | 0.9  | -9.3 dB  |
| Peaking | 277 Hz  | 1.2  | 11.6 dB  |
| Peaking | 3376 Hz | 0.74 | 4.5 dB   |
| Peaking | 1805 Hz | 2.88 | 2.0 dB   |
| Peaking | 2814 Hz | 4.88 | -2.6 dB  |
| Peaking | 4175 Hz | 2.01 | 8.9 dB   |
| Peaking | 5096 Hz | 1.31 | -10.8 dB |
| Peaking | 6158 Hz | 2.77 | 7.8 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sennheiser%20HD%20820/Sennheiser%20HD%20820.png)