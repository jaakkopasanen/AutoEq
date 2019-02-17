# Audio Technica ATH-R70x
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.4; 25 -2.2; 28 -3.2; 31 -4.1; 34 -4.8; 37 -5.4; 41 -6.1; 45 -6.7; 49 -7.1; 54 -7.6; 60 -8.1; 66 -8.4; 72 -8.7; 79 -9.0; 87 -9.1; 96 -8.8; 106 -9.4; 116 -9.7; 128 -9.9; 141 -9.9; 155 -10.0; 170 -9.9; 187 -9.9; 206 -9.8; 227 -9.5; 249 -9.4; 274 -9.2; 302 -9.0; 332 -8.7; 365 -8.5; 402 -8.2; 442 -7.9; 486 -8.0; 535 -7.8; 588 -7.4; 647 -7.3; 712 -7.5; 783 -7.0; 861 -7.2; 947 -7.1; 1042 -6.9; 1146 -7.1; 1261 -7.5; 1387 -8.2; 1526 -8.8; 1678 -9.4; 1846 -9.3; 2031 -8.8; 2234 -8.1; 2457 -7.0; 2703 -5.1; 2973 -4.5; 3270 -5.4; 3597 -7.4; 3957 -5.9; 4353 -4.6; 4788 -3.1; 5267 -1.1; 5793 -0.8; 6373 -1.2; 7010 -4.2; 7711 -6.4; 8482 -6.7; 9330 -8.0; 10263 -6.7; 11289 -6.7; 12418 -6.7; 13660 -6.7; 15026 -6.7; 16529 -6.7; 18182 -6.7; 20000 -6.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-R70x GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-R70x ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 19 Hz   |  1.14 | 6.6 dB  |
| Peaking | 143 Hz  |  0.46 | -3.4 dB |
| Peaking | 1808 Hz |  2.14 | -2.9 dB |
| Peaking | 2845 Hz |  6.83 | 3.2 dB  |
| Peaking | 5686 Hz |  2.88 | 6.8 dB  |
| Peaking | 30 Hz   |  1.62 | 0.4 dB  |
| Peaking | 1032 Hz |  4.67 | 0.5 dB  |
| Peaking | 3612 Hz | 13.66 | -1.6 dB |
| Peaking | 6570 Hz | 10.65 | 1.8 dB  |
| Peaking | 8922 Hz |  3.06 | -1.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.0 dB  |
| Peaking | 62 Hz    | 1.41 | -2.0 dB |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.8 dB |
| Peaking | 4000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-R70x/Audio%20Technica%20ATH-R70x.png)