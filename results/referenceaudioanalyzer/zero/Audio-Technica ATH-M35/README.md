# Audio-Technica ATH-M35
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.6; 34 -1.1; 37 -2.1; 41 -3.4; 45 -4.5; 49 -5.4; 54 -6.2; 60 -6.8; 66 -7.1; 72 -7.4; 79 -7.6; 87 -7.8; 96 -7.9; 106 -7.8; 116 -7.9; 128 -7.8; 141 -7.9; 155 -7.7; 170 -7.5; 187 -7.2; 206 -6.9; 227 -6.4; 249 -6.0; 274 -5.4; 302 -4.6; 332 -3.5; 365 -2.3; 402 -1.6; 442 -1.8; 486 -3.1; 535 -4.8; 588 -6.3; 647 -7.3; 712 -7.9; 783 -8.2; 861 -8.2; 947 -8.2; 1042 -8.2; 1146 -8.2; 1261 -8.4; 1387 -8.5; 1526 -8.5; 1678 -8.9; 1846 -9.3; 2031 -9.8; 2234 -10.2; 2457 -10.5; 2703 -10.2; 2973 -9.3; 3270 -8.8; 3597 -9.1; 3957 -9.0; 4353 -7.4; 4788 -3.8; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.2; 9330 -9.0; 10263 -10.5; 11289 -11.1; 12418 -10.8; 13660 -9.7; 15026 -7.1; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-M35 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-M35 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 26 Hz    | 1.78 | 7.2 dB  |
| Peaking | 410 Hz   | 2.7  | 5.9 dB  |
| Peaking | 3368 Hz  | 0.39 | -4.6 dB |
| Peaking | 5763 Hz  | 1.93 | 10.9 dB |
| Peaking | 11550 Hz | 1.67 | -4.5 dB |
| Peaking | 38 Hz    | 2.73 | 2.0 dB  |
| Peaking | 119 Hz   | 0.57 | -2.2 dB |
| Peaking | 488 Hz   | 0.31 | 1.4 dB  |
| Peaking | 736 Hz   | 1.65 | -2.1 dB |
| Peaking | 2419 Hz  | 4.5  | -0.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.0 dB  |
| Peaking | 62 Hz    | 1.41 | -1.7 dB |
| Peaking | 125 Hz   | 1.41 | -2.0 dB |
| Peaking | 250 Hz   | 1.41 | 0.9 dB  |
| Peaking | 500 Hz   | 1.41 | 3.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.2 dB |
| Peaking | 2000 Hz  | 1.41 | -3.7 dB |
| Peaking | 4000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -2.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Audio-Technica%20ATH-M35/Audio-Technica%20ATH-M35.png)