# Moondrop Blessing
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.7; 23 -7.2; 25 -7.4; 28 -7.3; 31 -7.2; 34 -7.2; 37 -7.2; 41 -7.1; 45 -7.0; 49 -6.9; 54 -7.0; 60 -7.1; 66 -7.3; 72 -7.1; 79 -7.3; 87 -7.2; 96 -6.9; 106 -7.2; 116 -6.9; 128 -7.1; 141 -6.8; 155 -6.8; 170 -6.8; 187 -6.8; 206 -6.8; 227 -6.7; 249 -6.7; 274 -6.6; 302 -6.4; 332 -6.2; 365 -6.0; 402 -5.9; 442 -5.8; 486 -5.6; 535 -5.4; 588 -5.2; 647 -5.1; 712 -4.8; 783 -4.5; 861 -4.4; 947 -4.5; 1042 -5.0; 1146 -5.7; 1261 -6.3; 1387 -6.6; 1526 -6.4; 1678 -6.1; 1846 -5.9; 2031 -5.6; 2234 -5.5; 2457 -5.5; 2703 -5.6; 2973 -5.1; 3270 -4.3; 3597 -4.0; 3957 -4.1; 4353 -4.5; 4788 -4.6; 5267 -4.3; 5793 -3.1; 6373 -0.5; 7010 -2.9; 7711 -5.1; 8482 -5.4; 9330 -5.4; 10263 -5.4; 11289 -5.4; 12418 -5.4; 13660 -12.5; 15026 -24.2; 16529 -28.8; 18182 -27.1; 20000 -26.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Moondrop Blessing GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Moondrop Blessing ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 56 Hz    | 0.23 | -1.8 dB  |
| Peaking | 1602 Hz  | 2.33 | -1.4 dB  |
| Peaking | 7218 Hz  | 0.31 | 19.4 dB  |
| Peaking | 12648 Hz | 1.51 | 16.1 dB  |
| Peaking | 15744 Hz | 0.24 | -36.7 dB |
| Peaking | 863 Hz   | 2.18 | 1.3 dB   |
| Peaking | 1271 Hz  | 4.15 | -0.9 dB  |
| Peaking | 5418 Hz  | 2.74 | -2.0 dB  |
| Peaking | 6379 Hz  | 4.36 | 4.2 dB   |
| Peaking | 7574 Hz  | 4.84 | -2.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -1.7 dB  |
| Peaking | 62 Hz    | 1.41 | -1.3 dB  |
| Peaking | 125 Hz   | 1.41 | -1.2 dB  |
| Peaking | 250 Hz   | 1.41 | -1.2 dB  |
| Peaking | 500 Hz   | 1.41 | 0.2 dB   |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB   |
| Peaking | 2000 Hz  | 1.41 | -1.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.4 dB   |
| Peaking | 8000 Hz  | 1.41 | 6.9 dB   |
| Peaking | 16000 Hz | 1.41 | -27.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Moondrop%20Blessing/Moondrop%20Blessing.png)