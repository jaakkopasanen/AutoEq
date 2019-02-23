# Audio Technica ATH-ANC7b
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.7; 23 -4.3; 25 -4.8; 28 -5.4; 31 -6.0; 34 -6.5; 37 -6.9; 41 -7.3; 45 -7.7; 49 -8.0; 54 -8.4; 60 -8.7; 66 -9.0; 72 -9.4; 79 -9.7; 87 -10.0; 96 -10.4; 106 -10.4; 116 -10.5; 128 -10.5; 141 -10.7; 155 -10.7; 170 -10.4; 187 -10.3; 206 -10.2; 227 -9.9; 249 -9.6; 274 -9.3; 302 -9.0; 332 -8.7; 365 -8.5; 402 -8.4; 442 -8.4; 486 -8.8; 535 -8.7; 588 -8.6; 647 -8.6; 712 -9.4; 783 -11.0; 861 -11.5; 947 -11.5; 1042 -11.7; 1146 -10.7; 1261 -6.5; 1387 -5.3; 1526 -5.8; 1678 -4.0; 1846 -4.0; 2031 -5.9; 2234 -3.0; 2457 -1.3; 2703 -1.2; 2973 -1.5; 3270 -1.1; 3597 -1.1; 3957 -1.7; 4353 -1.2; 4788 -0.5; 5267 -4.2; 5793 -3.5; 6373 -1.1; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -7.5; 10263 -8.3; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-ANC7b GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-ANC7b ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 17 Hz   |  1    | 3.8 dB  |
| Peaking | 134 Hz  |  0.43 | -4.2 dB |
| Peaking | 937 Hz  |  2.11 | -6.0 dB |
| Peaking | 2819 Hz |  0.96 | 4.7 dB  |
| Peaking | 4727 Hz |  1.69 | 3.1 dB  |
| Peaking | 1152 Hz |  6.33 | -3.9 dB |
| Peaking | 1234 Hz |  3.09 | 2.8 dB  |
| Peaking | 1985 Hz | 13.54 | -3.1 dB |
| Peaking | 6446 Hz | 10.62 | 3.7 dB  |
| Peaking | 9818 Hz |  3.55 | -2.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.5 dB  |
| Peaking | 62 Hz    | 1.41 | -2.2 dB |
| Peaking | 125 Hz   | 1.41 | -3.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | -5.3 dB |
| Peaking | 2000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-ANC7b/Audio%20Technica%20ATH-ANC7b.png)