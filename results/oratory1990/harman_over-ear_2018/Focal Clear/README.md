# Focal Clear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.8; 23 -1.0; 25 -1.2; 28 -1.5; 31 -1.7; 34 -1.9; 37 -2.1; 41 -2.3; 45 -2.4; 49 -2.6; 54 -2.9; 60 -3.1; 66 -3.4; 72 -3.7; 79 -4.0; 87 -4.4; 96 -4.7; 106 -5.1; 116 -5.4; 128 -5.7; 141 -5.9; 155 -6.0; 170 -6.1; 187 -6.1; 206 -6.1; 227 -6.0; 249 -5.9; 274 -5.7; 302 -5.5; 332 -5.3; 365 -5.0; 402 -4.9; 442 -4.9; 486 -4.8; 535 -4.8; 588 -4.8; 647 -4.9; 712 -5.2; 783 -5.5; 861 -6.0; 947 -6.5; 1042 -7.0; 1146 -7.7; 1261 -8.2; 1387 -8.2; 1526 -7.6; 1678 -6.6; 1846 -5.6; 2031 -4.8; 2234 -4.3; 2457 -4.6; 2703 -5.1; 2973 -5.7; 3270 -5.3; 3597 -5.0; 3957 -1.9; 4353 -0.5; 4788 -1.2; 5267 -1.8; 5793 -5.2; 6373 -1.0; 7010 -2.3; 7711 -4.5; 8482 -4.7; 9330 -4.8; 10263 -4.8; 11289 -5.2; 12418 -7.7; 13660 -5.4; 15026 -4.8; 16529 -7.5; 18182 -10.7; 20000 -13.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Clear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Clear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.3dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 23 Hz    |  1.34 | 3.9 dB  |
| Peaking | 48 Hz    |  2.09 | 1.8 dB  |
| Peaking | 2217 Hz  |  1.92 | 6.9 dB  |
| Peaking | 2268 Hz  |  0.69 | -7.1 dB |
| Peaking | 4497 Hz  |  1.6  | 6.6 dB  |
| Peaking | 184 Hz   |  1.28 | -1.5 dB |
| Peaking | 588 Hz   |  1.99 | 1.0 dB  |
| Peaking | 6646 Hz  | 11.92 | 4.1 dB  |
| Peaking | 19235 Hz |  0.86 | -6.5 dB |
| Peaking | 20348 Hz |  1.32 | -3.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.6 dB  |
| Peaking | 62 Hz    | 1.41 | 1.2 dB  |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.6 dB |
| Peaking | 2000 Hz  | 1.41 | -1.4 dB |
| Peaking | 4000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -3.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Focal%20Clear/Focal%20Clear.png)