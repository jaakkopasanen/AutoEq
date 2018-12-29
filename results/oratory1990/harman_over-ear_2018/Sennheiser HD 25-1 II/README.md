# Sennheiser HD 25-1 II

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 5.4; 79 4.0; 87 2.9; 96 1.8; 106 0.8; 116 0.2; 128 0.3; 141 0.3; 155 -0.1; 170 -0.1; 187 -0.3; 206 -0.4; 227 -0.6; 249 -0.6; 274 -0.5; 302 -0.3; 332 0.0; 365 0.5; 402 1.2; 442 1.4; 486 1.6; 535 2.0; 588 2.1; 647 2.1; 712 1.8; 783 1.2; 861 0.5; 947 0.2; 1042 -0.2; 1146 -0.3; 1261 0.9; 1387 0.5; 1526 0.3; 1678 -0.1; 1846 -0.5; 2031 -0.8; 2234 -1.1; 2457 -1.3; 2703 -1.2; 2973 -1.0; 3270 0.1; 3597 1.1; 3957 1.7; 4353 6.0; 4788 4.1; 5267 2.8; 5793 4.7; 6373 -0.3; 7010 -2.7; 7711 -4.4; 8482 -6.2; 9330 -4.7; 10263 -0.2; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 25-1 II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 25-1 II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 37 Hz    | 0.71 | 7.1 dB  |
| Peaking | 601 Hz   | 2.2  | 2.4 dB  |
| Peaking | 3104 Hz  | 1.3  | -4.0 dB |
| Peaking | 4560 Hz  | 1.28 | 7.2 dB  |
| Peaking | 8192 Hz  | 2.63 | -7.8 dB |
| Peaking | 42 Hz    | 3.01 | -1.3 dB |
| Peaking | 69 Hz    | 2.41 | 2.7 dB  |
| Peaking | 140 Hz   | 0.78 | -1.3 dB |
| Peaking | 1338 Hz  | 6.45 | 0.8 dB  |
| Peaking | 10656 Hz | 7.27 | 1.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sennheiser%20HD%2025-1%20II/Sennheiser%20HD%2025-1%20II.png)