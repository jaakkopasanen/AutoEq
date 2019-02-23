# Massdrop x Fostex TH-X00
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.6; 23 -3.7; 25 -4.7; 28 -5.7; 31 -6.4; 34 -6.7; 37 -7.0; 41 -7.0; 45 -7.1; 49 -7.1; 54 -7.1; 60 -7.0; 66 -7.0; 72 -7.1; 79 -7.2; 87 -7.4; 96 -7.6; 106 -7.8; 116 -8.0; 128 -8.2; 141 -8.3; 155 -8.4; 170 -8.4; 187 -8.4; 206 -8.4; 227 -8.4; 249 -8.2; 274 -8.0; 302 -7.7; 332 -7.4; 365 -7.1; 402 -6.7; 442 -6.3; 486 -5.9; 535 -5.3; 588 -4.9; 647 -6.0; 712 -7.8; 783 -7.2; 861 -6.7; 947 -7.9; 1042 -8.0; 1146 -7.8; 1261 -7.9; 1387 -8.1; 1526 -8.2; 1678 -7.9; 1846 -7.6; 2031 -7.3; 2234 -7.1; 2457 -7.0; 2703 -6.2; 2973 -1.0; 3270 -1.1; 3597 -0.5; 3957 -1.5; 4353 -4.8; 4788 -7.9; 5267 -9.1; 5793 -8.2; 6373 -3.7; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -8.7; 11289 -12.2; 12418 -14.9; 13660 -14.1; 15026 -10.7; 16529 -9.3; 18182 -10.8; 20000 -14.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop x Fostex TH-X00 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x Fostex TH-X00 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 22 Hz    | 3.65 | 4.6 dB   |
| Peaking | 3440 Hz  | 1.71 | 15.1 dB  |
| Peaking | 3669 Hz  | 0.54 | -12.0 dB |
| Peaking | 9033 Hz  | 0.4  | 23.5 dB  |
| Peaking | 11863 Hz | 0.42 | -24.3 dB |
| Peaking | 172 Hz   | 0.6  | -1.9 dB  |
| Peaking | 547 Hz   | 3.29 | 2.3 dB   |
| Peaking | 5510 Hz  | 4.57 | -2.9 dB  |
| Peaking | 6674 Hz  | 5.62 | 4.9 dB   |
| Peaking | 9227 Hz  | 3.04 | -1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.8 dB  |
| Peaking | 62 Hz    | 1.41 | -0.5 dB |
| Peaking | 125 Hz   | 1.41 | -1.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.0 dB |
| Peaking | 500 Hz   | 1.41 | 1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.6 dB |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB |
| Peaking | 4000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | -7.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Massdrop%20x%20Fostex%20TH-X00/Massdrop%20x%20Fostex%20TH-X00.png)