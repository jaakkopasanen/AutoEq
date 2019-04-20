# Superlux HD-651
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.6; 72 -0.9; 79 -1.0; 87 -1.5; 96 -2.0; 106 -1.9; 116 -2.5; 128 -3.6; 141 -4.6; 155 -4.9; 170 -5.4; 187 -7.0; 206 -8.0; 227 -8.0; 249 -8.0; 274 -9.5; 302 -10.9; 332 -10.5; 365 -10.7; 402 -10.5; 442 -10.1; 486 -9.5; 535 -9.1; 588 -8.5; 647 -8.0; 712 -7.9; 783 -7.9; 861 -8.2; 947 -8.5; 1042 -7.1; 1146 -6.6; 1261 -7.6; 1387 -7.8; 1526 -7.9; 1678 -7.9; 1846 -7.5; 2031 -7.1; 2234 -6.0; 2457 -4.0; 2703 -7.3; 2973 -8.6; 3270 -7.7; 3597 -4.6; 3957 -1.2; 4353 -2.6; 4788 -11.4; 5267 -7.1; 5793 -3.8; 6373 -4.8; 7010 -7.4; 7711 -6.7; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Superlux HD-651 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Superlux HD-651 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 44 Hz   |  0.23 | 6.5 dB  |
| Peaking | 317 Hz  |  0.75 | -5.8 dB |
| Peaking | 1576 Hz |  3.54 | -1.3 dB |
| Peaking | 4128 Hz |  6.14 | 7.3 dB  |
| Peaking | 4748 Hz | 10.24 | -7.2 dB |
| Peaking | 1215 Hz |  4.22 | 0.3 dB  |
| Peaking | 2154 Hz |  3.47 | -0.9 dB |
| Peaking | 2426 Hz |  6.01 | 3.9 dB  |
| Peaking | 2945 Hz |  4.93 | -3.1 dB |
| Peaking | 5898 Hz |  8.41 | 3.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 5.0 dB  |
| Peaking | 125 Hz   | 1.41 | 3.2 dB  |
| Peaking | 250 Hz   | 1.41 | -3.3 dB |
| Peaking | 500 Hz   | 1.41 | -2.9 dB |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | -0.8 dB |
| Peaking | 4000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Superlux%20HD-651/Superlux%20HD-651.png)