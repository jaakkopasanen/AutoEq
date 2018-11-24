# Sennheiser HD 650

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 5.7; 41 5.2; 45 5.0; 49 4.8; 54 4.4; 60 4.1; 66 3.5; 72 2.7; 79 1.8; 87 1.1; 96 0.4; 106 -0.2; 116 -0.6; 128 -1.0; 141 -1.4; 155 -1.6; 170 -1.7; 187 -1.8; 206 -1.9; 227 -1.8; 249 -1.6; 274 -1.4; 302 -1.2; 332 -1.0; 365 -0.7; 402 -0.5; 442 -0.4; 486 -0.3; 535 0.0; 588 0.2; 647 0.2; 712 0.2; 783 0.1; 861 0.1; 947 0.2; 1042 -0.1; 1146 -0.0; 1261 0.2; 1387 0.6; 1526 1.0; 1678 1.3; 1846 1.8; 2031 2.1; 2234 2.2; 2457 1.6; 2703 0.8; 2973 0.3; 3270 0.4; 3597 1.5; 3957 3.0; 4353 4.3; 4788 2.3; 5267 2.0; 5793 4.0; 6373 3.0; 7010 2.4; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 -0.8; 15026 -2.4; 16529 -5.0; 18182 -7.1; 20000 -5.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 650 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 650 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 31 Hz    |  0.93 | 6.8 dB  |
| Peaking | 2021 Hz  |  3.02 | 2.0 dB  |
| Peaking | 5266 Hz  |  1.32 | 3.4 dB  |
| Peaking | 18571 Hz |  1.18 | -7.8 dB |
| Peaking | 24000 Hz |  1.76 | 2.0 dB  |
| Peaking | 63 Hz    |  2.37 | 2.0 dB  |
| Peaking | 180 Hz   |  0.9  | -2.3 dB |
| Peaking | 3128 Hz  |  5.6  | -1.2 dB |
| Peaking | 4197 Hz  | 10.38 | 2.0 dB  |
| Peaking | 12887 Hz |  5.33 | 1.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sennheiser%20HD%20650/Sennheiser%20HD%20650.png)