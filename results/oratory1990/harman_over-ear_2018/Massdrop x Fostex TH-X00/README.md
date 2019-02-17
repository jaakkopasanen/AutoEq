# Massdrop x Fostex TH-X00
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.0; 23 -2.2; 25 -3.2; 28 -4.2; 31 -4.8; 34 -5.2; 37 -5.4; 41 -5.5; 45 -5.5; 49 -5.6; 54 -5.6; 60 -5.5; 66 -5.5; 72 -5.6; 79 -5.7; 87 -5.9; 96 -6.0; 106 -6.3; 116 -6.5; 128 -6.7; 141 -6.8; 155 -6.9; 170 -6.9; 187 -6.9; 206 -6.9; 227 -6.8; 249 -6.7; 274 -6.5; 302 -6.2; 332 -5.9; 365 -5.6; 402 -5.2; 442 -4.8; 486 -4.4; 535 -3.8; 588 -3.4; 647 -4.5; 712 -6.3; 783 -5.7; 861 -5.2; 947 -6.3; 1042 -6.5; 1146 -6.3; 1261 -6.4; 1387 -6.6; 1526 -6.6; 1678 -6.4; 1846 -6.1; 2031 -5.7; 2234 -5.6; 2457 -5.5; 2703 -4.7; 2973 -0.6; 3270 -0.5; 3597 -0.5; 3957 -0.6; 4353 -3.3; 4788 -6.4; 5267 -7.6; 5793 -6.6; 6373 -2.2; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -7.2; 11289 -10.7; 12418 -13.4; 13660 -12.6; 15026 -9.2; 16529 -7.8; 18182 -9.3; 20000 -13.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop x Fostex TH-X00 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x Fostex TH-X00 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 16 Hz    |  1.2  | 8.9 dB  |
| Peaking | 546 Hz   |  2.55 | 3.0 dB  |
| Peaking | 3448 Hz  |  2.7  | 7.1 dB  |
| Peaking | 6599 Hz  |  7.99 | 4.9 dB  |
| Peaking | 12984 Hz |  2.06 | -7.5 dB |
| Peaking | 75 Hz    |  2.23 | 0.7 dB  |
| Peaking | 173 Hz   |  1.62 | -0.6 dB |
| Peaking | 4096 Hz  | 10    | 2.3 dB  |
| Peaking | 5237 Hz  |  5.45 | -2.6 dB |
| Peaking | 9674 Hz  |  5.08 | 1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.4 dB  |
| Peaking | 62 Hz    | 1.41 | 0.6 dB  |
| Peaking | 125 Hz   | 1.41 | -0.2 dB |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | 2.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | -0.0 dB |
| Peaking | 4000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | -5.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Massdrop%20x%20Fostex%20TH-X00/Massdrop%20x%20Fostex%20TH-X00.png)