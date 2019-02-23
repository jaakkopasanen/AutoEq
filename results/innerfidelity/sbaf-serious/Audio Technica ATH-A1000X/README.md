# Audio Technica ATH-A1000X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.2; 23 -3.0; 25 -3.8; 28 -4.8; 31 -5.6; 34 -6.4; 37 -7.1; 41 -7.8; 45 -8.3; 49 -8.8; 54 -9.2; 60 -9.5; 66 -9.6; 72 -9.3; 79 -8.9; 87 -9.0; 96 -8.7; 106 -9.3; 116 -10.4; 128 -11.0; 141 -10.8; 155 -9.9; 170 -9.0; 187 -9.8; 206 -9.2; 227 -8.4; 249 -7.9; 274 -7.6; 302 -7.6; 332 -7.6; 365 -7.7; 402 -7.9; 442 -7.9; 486 -8.2; 535 -8.3; 588 -8.1; 647 -8.2; 712 -8.4; 783 -8.4; 861 -8.4; 947 -8.7; 1042 -8.8; 1146 -9.0; 1261 -8.7; 1387 -9.3; 1526 -9.1; 1678 -8.9; 1846 -10.3; 2031 -13.0; 2234 -10.6; 2457 -7.7; 2703 -5.1; 2973 -1.1; 3270 -0.6; 3597 -0.5; 3957 -1.3; 4353 -4.6; 4788 -2.9; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -8.5; 10263 -7.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -8.5; 18182 -11.6; 20000 -8.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-A1000X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-A1000X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 21 Hz    | 1.68 | 5.0 dB   |
| Peaking | 104 Hz   | 0.45 | -3.5 dB  |
| Peaking | 2538 Hz  | 0.78 | -10.4 dB |
| Peaking | 3183 Hz  | 1.62 | 15.1 dB  |
| Peaking | 5767 Hz  | 2.99 | 6.9 dB   |
| Peaking | 134 Hz   | 7.08 | -1.4 dB  |
| Peaking | 1925 Hz  | 2.44 | 3.2 dB   |
| Peaking | 2018 Hz  | 5.56 | -5.7 dB  |
| Peaking | 9562 Hz  | 6.95 | -2.7 dB  |
| Peaking | 18500 Hz | 1.54 | -5.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.8 dB  |
| Peaking | 62 Hz    | 1.41 | -2.6 dB |
| Peaking | 125 Hz   | 1.41 | -3.5 dB |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | -1.4 dB |
| Peaking | 2000 Hz  | 1.41 | -5.1 dB |
| Peaking | 4000 Hz  | 1.41 | 7.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -2.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-A1000X/Audio%20Technica%20ATH-A1000X.png)