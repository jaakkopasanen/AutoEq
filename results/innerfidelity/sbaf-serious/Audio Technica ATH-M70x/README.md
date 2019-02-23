# Audio Technica ATH-M70x
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.3; 23 -5.7; 25 -6.1; 28 -6.6; 31 -6.9; 34 -7.1; 37 -7.2; 41 -7.3; 45 -7.2; 49 -6.8; 54 -6.1; 60 -5.4; 66 -4.8; 72 -3.6; 79 -2.0; 87 -0.9; 96 -1.8; 106 -4.5; 116 -6.4; 128 -6.2; 141 -4.4; 155 -3.0; 170 -3.1; 187 -5.3; 206 -4.4; 227 -4.3; 249 -4.4; 274 -4.1; 302 -3.8; 332 -3.6; 365 -3.3; 402 -3.2; 442 -2.8; 486 -2.7; 535 -2.5; 588 -1.7; 647 -0.9; 712 -2.1; 783 -2.9; 861 -3.9; 947 -4.3; 1042 -4.6; 1146 -4.9; 1261 -5.3; 1387 -5.9; 1526 -6.8; 1678 -7.7; 1846 -8.1; 2031 -8.0; 2234 -7.3; 2457 -5.8; 2703 -3.9; 2973 -3.2; 3270 -4.2; 3597 -5.0; 3957 -5.6; 4353 -8.7; 4788 -8.3; 5267 -5.6; 5793 -1.5; 6373 -0.5; 7010 -2.2; 7711 -5.2; 8482 -8.6; 9330 -10.1; 10263 -8.3; 11289 -4.7; 12418 -4.7; 13660 -4.7; 15026 -4.7; 16529 -4.7; 18182 -4.7; 20000 -4.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-M70x GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-M70x ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.5dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 87 Hz   | 6.54 | 4.3 dB   |
| Peaking | 1878 Hz | 0.78 | -13.3 dB |
| Peaking | 2619 Hz | 0.27 | 10.6 dB  |
| Peaking | 4508 Hz | 3.17 | -9.7 dB  |
| Peaking | 9267 Hz | 2.39 | -9.9 dB  |
| Peaking | 38 Hz   | 1.35 | -3.4 dB  |
| Peaking | 155 Hz  | 0.2  | 1.4 dB   |
| Peaking | 266 Hz  | 0.25 | -1.6 dB  |
| Peaking | 630 Hz  | 4.8  | 2.2 dB   |
| Peaking | 6350 Hz | 7.43 | 2.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.3 dB |
| Peaking | 62 Hz    | 1.41 | 1.2 dB  |
| Peaking | 125 Hz   | 1.41 | 0.2 dB  |
| Peaking | 250 Hz   | 1.41 | -0.2 dB |
| Peaking | 500 Hz   | 1.41 | 2.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.9 dB |
| Peaking | 4000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-M70x/Audio%20Technica%20ATH-M70x.png)