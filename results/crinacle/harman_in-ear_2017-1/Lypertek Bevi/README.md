# Lypertek Bevi
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.9; 23 -1.2; 25 -1.5; 28 -1.8; 31 -2.0; 34 -2.2; 37 -2.3; 41 -2.5; 45 -2.6; 49 -2.8; 54 -3.1; 60 -3.4; 66 -3.6; 72 -4.0; 79 -4.3; 87 -4.7; 96 -5.2; 106 -5.5; 116 -6.0; 128 -6.3; 141 -6.5; 155 -6.8; 170 -7.0; 187 -7.2; 206 -7.3; 227 -7.4; 249 -7.4; 274 -7.4; 302 -7.3; 332 -7.1; 365 -7.0; 402 -6.9; 442 -6.7; 486 -6.5; 535 -6.3; 588 -6.1; 647 -5.8; 712 -5.4; 783 -5.1; 861 -4.8; 947 -4.7; 1042 -5.0; 1146 -5.6; 1261 -6.0; 1387 -5.9; 1526 -5.4; 1678 -4.6; 1846 -3.7; 2031 -2.6; 2234 -1.3; 2457 -0.8; 2703 -0.6; 2973 -0.7; 3270 -1.1; 3597 -1.5; 3957 -1.8; 4353 -1.4; 4788 -1.1; 5267 -0.9; 5793 -0.8; 6373 -0.5; 7010 -2.0; 7711 -4.2; 8482 -4.7; 9330 -4.5; 10263 -4.5; 11289 -4.5; 12418 -4.5; 13660 -9.2; 15026 -18.3; 16529 -22.2; 18182 -17.9; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Lypertek Bevi GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Lypertek Bevi ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 15 Hz    | 0.16 | 3.5 dB   |
| Peaking | 213 Hz   | 0.35 | -3.3 dB  |
| Peaking | 2756 Hz  | 2    | 3.2 dB   |
| Peaking | 11287 Hz | 0.37 | 7.4 dB   |
| Peaking | 16496 Hz | 0.88 | -24.0 dB |
| Peaking | 1382 Hz  | 4.23 | -1.8 dB  |
| Peaking | 6480 Hz  | 1.9  | 3.5 dB   |
| Peaking | 7931 Hz  | 1.98 | -4.3 dB  |
| Peaking | 12871 Hz | 3.32 | 4.1 dB   |
| Peaking | 14920 Hz | 4.28 | -3.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 3.1 dB   |
| Peaking | 62 Hz    | 1.41 | 0.9 dB   |
| Peaking | 125 Hz   | 1.41 | -1.5 dB  |
| Peaking | 250 Hz   | 1.41 | -2.8 dB  |
| Peaking | 500 Hz   | 1.41 | -1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.4 dB   |
| Peaking | 4000 Hz  | 1.41 | 3.9 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.3 dB   |
| Peaking | 16000 Hz | 1.41 | -18.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Lypertek%20Bevi/Lypertek%20Bevi.png)