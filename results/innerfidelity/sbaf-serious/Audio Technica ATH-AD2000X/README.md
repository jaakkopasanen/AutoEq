# Audio Technica ATH-AD2000X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.6; 34 -1.0; 37 -1.4; 41 -2.0; 45 -2.5; 49 -2.9; 54 -3.3; 60 -3.7; 66 -4.1; 72 -4.5; 79 -5.0; 87 -5.4; 96 -5.9; 106 -6.5; 116 -7.1; 128 -7.5; 141 -7.9; 155 -8.1; 170 -8.3; 187 -8.6; 206 -8.8; 227 -8.9; 249 -8.9; 274 -8.9; 302 -9.0; 332 -9.0; 365 -9.1; 402 -9.0; 442 -9.0; 486 -9.2; 535 -9.2; 588 -9.1; 647 -9.2; 712 -9.2; 783 -9.3; 861 -9.5; 947 -9.7; 1042 -9.8; 1146 -9.8; 1261 -9.5; 1387 -9.5; 1526 -9.2; 1678 -8.5; 1846 -6.9; 2031 -5.2; 2234 -3.2; 2457 -0.8; 2703 -0.5; 2973 -0.5; 3270 -0.8; 3597 -5.8; 3957 -7.5; 4353 -5.6; 4788 -1.9; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.6; 9330 -7.7; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-AD2000X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-AD2000X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 0.43 | 6.2 dB  |
| Peaking | 922 Hz  | 0.12 | -3.3 dB |
| Peaking | 2692 Hz | 2.25 | 9.6 dB  |
| Peaking | 5747 Hz | 2.35 | 8.4 dB  |
| Peaking | 8794 Hz | 2.93 | -0.9 dB |
| Peaking | 1392 Hz | 1.06 | -4.0 dB |
| Peaking | 2097 Hz | 0.51 | 4.4 dB  |
| Peaking | 3277 Hz | 5.9  | 6.4 dB  |
| Peaking | 3534 Hz | 1.43 | -6.9 dB |
| Peaking | 4853 Hz | 6.92 | 3.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 1.8 dB  |
| Peaking | 125 Hz   | 1.41 | -1.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | -1.5 dB |
| Peaking | 1000 Hz  | 1.41 | -4.3 dB |
| Peaking | 2000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-AD2000X/Audio%20Technica%20ATH-AD2000X.png)