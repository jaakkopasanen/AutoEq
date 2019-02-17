# Final Audio Pandora Hope 4
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.0; 23 -10.1; 25 -10.2; 28 -10.2; 31 -10.1; 34 -10.0; 37 -9.9; 41 -9.6; 45 -9.2; 49 -8.8; 54 -8.7; 60 -9.3; 66 -9.9; 72 -10.3; 79 -10.2; 87 -9.5; 96 -8.6; 106 -7.3; 116 -7.9; 128 -10.0; 141 -9.9; 155 -8.8; 170 -7.8; 187 -8.9; 206 -8.8; 227 -8.6; 249 -8.9; 274 -8.6; 302 -8.2; 332 -7.8; 365 -7.8; 402 -7.4; 442 -7.2; 486 -7.2; 535 -7.1; 588 -6.5; 647 -6.4; 712 -7.2; 783 -7.3; 861 -7.2; 947 -6.8; 1042 -6.3; 1146 -5.9; 1261 -5.9; 1387 -6.1; 1526 -6.3; 1678 -6.1; 1846 -5.6; 2031 -5.1; 2234 -5.2; 2457 -4.8; 2703 -3.0; 2973 -0.5; 3270 -2.7; 3597 -1.1; 3957 -5.0; 4353 -7.0; 4788 -4.9; 5267 -0.8; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -7.9; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Final Audio Pandora Hope 4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Final Audio Pandora Hope 4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.77 | -3.7 dB |
| Peaking | 74 Hz   | 3.25 | -2.5 dB |
| Peaking | 191 Hz  | 0.71 | -2.3 dB |
| Peaking | 3050 Hz | 2.95 | 5.6 dB  |
| Peaking | 5875 Hz | 3.87 | 6.6 dB  |
| Peaking | 110 Hz  | 7.58 | 1.7 dB  |
| Peaking | 131 Hz  | 8.14 | -1.9 dB |
| Peaking | 3685 Hz | 9.11 | 3.0 dB  |
| Peaking | 4211 Hz | 7.82 | -3.5 dB |
| Peaking | 9173 Hz | 6.15 | -1.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.5 dB |
| Peaking | 62 Hz    | 1.41 | -2.2 dB |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | -1.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Final%20Audio%20Pandora%20Hope%204/Final%20Audio%20Pandora%20Hope%204.png)