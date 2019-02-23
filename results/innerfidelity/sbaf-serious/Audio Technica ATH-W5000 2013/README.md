# Audio Technica ATH-W5000 2013
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.7; 49 -1.7; 54 -3.0; 60 -4.4; 66 -5.2; 72 -5.4; 79 -6.2; 87 -7.7; 96 -8.5; 106 -8.9; 116 -8.9; 128 -9.2; 141 -9.2; 155 -9.2; 170 -8.9; 187 -8.9; 206 -8.9; 227 -8.7; 249 -8.7; 274 -8.7; 302 -8.5; 332 -7.8; 365 -7.2; 402 -6.4; 442 -4.7; 486 -3.7; 535 -3.4; 588 -3.7; 647 -5.0; 712 -6.0; 783 -6.4; 861 -7.4; 947 -8.2; 1042 -9.0; 1146 -9.5; 1261 -9.9; 1387 -10.3; 1526 -10.7; 1678 -9.7; 1846 -9.3; 2031 -9.9; 2234 -9.2; 2457 -6.1; 2703 -2.9; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -5.2; 4353 -7.0; 4788 -7.9; 5267 -4.3; 5793 -2.3; 6373 -1.7; 7010 -4.0; 7711 -6.2; 8482 -7.6; 9330 -10.5; 10263 -9.7; 11289 -7.1; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.6; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-W5000 2013 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-W5000 2013 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 1.38 | 7.3 dB  |
| Peaking | 1702 Hz | 1.22 | -4.7 dB |
| Peaking | 3117 Hz | 3.04 | 8.3 dB  |
| Peaking | 6334 Hz | 4.11 | 5.4 dB  |
| Peaking | 9562 Hz | 3.67 | -4.6 dB |
| Peaking | 51 Hz   | 1.49 | 3.6 dB  |
| Peaking | 149 Hz  | 0.38 | -3.2 dB |
| Peaking | 531 Hz  | 1.97 | 4.9 dB  |
| Peaking | 1095 Hz | 3.82 | -1.1 dB |
| Peaking | 4610 Hz | 7.9  | -2.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.6 dB  |
| Peaking | 62 Hz    | 1.41 | 1.3 dB  |
| Peaking | 125 Hz   | 1.41 | -3.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.9 dB |
| Peaking | 500 Hz   | 1.41 | 3.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.9 dB |
| Peaking | 2000 Hz  | 1.41 | -2.8 dB |
| Peaking | 4000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-W5000%202013/Audio%20Technica%20ATH-W5000%202013.png)