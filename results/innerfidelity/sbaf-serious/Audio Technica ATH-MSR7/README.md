# Audio Technica ATH-MSR7
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.4; 23 -1.9; 25 -2.4; 28 -2.9; 31 -3.4; 34 -3.7; 37 -4.0; 41 -4.4; 45 -4.6; 49 -4.9; 54 -5.1; 60 -5.4; 66 -5.7; 72 -6.0; 79 -6.3; 87 -6.7; 96 -7.1; 106 -7.3; 116 -7.5; 128 -7.8; 141 -7.9; 155 -8.2; 170 -8.0; 187 -7.7; 206 -7.9; 227 -7.9; 249 -7.9; 274 -7.6; 302 -7.3; 332 -6.8; 365 -6.1; 402 -5.5; 442 -5.0; 486 -5.0; 535 -5.1; 588 -5.1; 647 -5.9; 712 -6.8; 783 -7.2; 861 -7.9; 947 -8.4; 1042 -8.6; 1146 -8.8; 1261 -9.0; 1387 -9.7; 1526 -10.4; 1678 -10.8; 1846 -10.7; 2031 -9.9; 2234 -8.1; 2457 -6.5; 2703 -5.0; 2973 -3.7; 3270 -3.2; 3597 -3.1; 3957 -3.9; 4353 -7.2; 4788 -7.3; 5267 -3.2; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -8.1; 10263 -7.4; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-MSR7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-MSR7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 14 Hz    | 0.53 | 5.8 dB  |
| Peaking | 150 Hz   | 1.22 | -1.9 dB |
| Peaking | 1691 Hz  | 1.48 | -4.8 dB |
| Peaking | 3164 Hz  | 2.68 | 4.5 dB  |
| Peaking | 6029 Hz  | 4.72 | 6.8 dB  |
| Peaking | 282 Hz   | 1.45 | -2.3 dB |
| Peaking | 570 Hz   | 0.62 | 3.6 dB  |
| Peaking | 871 Hz   | 1.24 | -3.4 dB |
| Peaking | 4601 Hz  | 9.12 | -2.9 dB |
| Peaking | 20796 Hz | 1.85 | -0.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.0 dB  |
| Peaking | 62 Hz    | 1.41 | 0.4 dB  |
| Peaking | 125 Hz   | 1.41 | -1.4 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | 2.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.4 dB |
| Peaking | 2000 Hz  | 1.41 | -3.4 dB |
| Peaking | 4000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-MSR7/Audio%20Technica%20ATH-MSR7.png)