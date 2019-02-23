# Audio Technica ATH-ES55
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.9; 79 -1.9; 87 -2.8; 96 -3.1; 106 -3.4; 116 -4.2; 128 -5.4; 141 -5.9; 155 -6.3; 170 -6.3; 187 -6.9; 206 -7.2; 227 -7.5; 249 -7.7; 274 -7.4; 302 -6.8; 332 -6.9; 365 -7.3; 402 -7.3; 442 -7.1; 486 -7.2; 535 -7.1; 588 -7.0; 647 -7.4; 712 -8.0; 783 -8.5; 861 -9.2; 947 -9.6; 1042 -10.0; 1146 -10.3; 1261 -10.6; 1387 -11.2; 1526 -11.8; 1678 -12.0; 1846 -11.4; 2031 -10.4; 2234 -9.0; 2457 -7.0; 2703 -5.6; 2973 -4.5; 3270 -4.4; 3597 -4.8; 3957 -4.4; 4353 -4.2; 4788 -2.2; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.3; 8482 -7.0; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.3; 15026 -11.1; 16529 -10.9; 18182 -8.7; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-ES55 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-ES55 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 39 Hz    | 0.58 | 6.9 dB  |
| Peaking | 1897 Hz  | 0.71 | -7.4 dB |
| Peaking | 2866 Hz  | 1.43 | 6.5 dB  |
| Peaking | 5610 Hz  | 2.35 | 7.2 dB  |
| Peaking | 16124 Hz | 1.68 | -5.3 dB |
| Peaking | 38 Hz    | 1.15 | -3.8 dB |
| Peaking | 52 Hz    | 0.12 | 3.0 dB  |
| Peaking | 191 Hz   | 0.69 | -3.8 dB |
| Peaking | 8172 Hz  | 7.18 | -1.7 dB |
| Peaking | 12898 Hz | 4.72 | 1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 5.3 dB  |
| Peaking | 125 Hz   | 1.41 | 0.7 dB  |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.2 dB |
| Peaking | 2000 Hz  | 1.41 | -4.7 dB |
| Peaking | 4000 Hz  | 1.41 | 5.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 16000 Hz | 1.41 | -5.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-ES55/Audio%20Technica%20ATH-ES55.png)