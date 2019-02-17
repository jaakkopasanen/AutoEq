# Nu Force HP-800
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.9; 23 -8.7; 25 -9.4; 28 -10.2; 31 -10.8; 34 -11.2; 37 -11.5; 41 -11.8; 45 -12.1; 49 -12.3; 54 -12.3; 60 -12.3; 66 -12.4; 72 -12.6; 79 -13.0; 87 -13.2; 96 -13.4; 106 -13.6; 116 -13.6; 128 -13.8; 141 -13.8; 155 -13.7; 170 -13.4; 187 -13.4; 206 -13.1; 227 -12.8; 249 -12.6; 274 -11.8; 302 -10.8; 332 -9.8; 365 -7.7; 402 -6.1; 442 -6.5; 486 -6.3; 535 -6.3; 588 -7.3; 647 -7.7; 712 -7.5; 783 -6.8; 861 -6.3; 947 -6.0; 1042 -5.7; 1146 -5.4; 1261 -5.5; 1387 -6.1; 1526 -7.1; 1678 -8.3; 1846 -9.3; 2031 -10.2; 2234 -11.1; 2457 -12.2; 2703 -12.7; 2973 -11.8; 3270 -10.3; 3597 -8.8; 3957 -7.3; 4353 -6.1; 4788 -3.2; 5267 -0.5; 5793 -1.7; 6373 -3.3; 7010 -6.8; 7711 -5.8; 8482 -5.8; 9330 -6.3; 10263 -5.9; 11289 -5.9; 12418 -5.9; 13660 -5.9; 15026 -5.9; 16529 -5.9; 18182 -5.9; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Nu Force HP-800 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Nu Force HP-800 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 54 Hz   |  0.5  | -5.8 dB |
| Peaking | 143 Hz  |  1.04 | -5.1 dB |
| Peaking | 248 Hz  |  2.18 | -3.9 dB |
| Peaking | 2658 Hz |  1.7  | -7.2 dB |
| Peaking | 5382 Hz |  3.86 | 6.8 dB  |
| Peaking | 415 Hz  |  6.69 | 1.8 dB  |
| Peaking | 673 Hz  |  4.67 | -1.5 dB |
| Peaking | 1228 Hz |  2.26 | 1.6 dB  |
| Peaking | 1804 Hz |  3.77 | -1.1 dB |
| Peaking | 7120 Hz | 12.18 | -1.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.3 dB |
| Peaking | 62 Hz    | 1.41 | -5.1 dB |
| Peaking | 125 Hz   | 1.41 | -6.7 dB |
| Peaking | 250 Hz   | 1.41 | -5.5 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.7 dB |
| Peaking | 4000 Hz  | 1.41 | -0.2 dB |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Nu%20Force%20HP-800/Nu%20Force%20HP-800.png)