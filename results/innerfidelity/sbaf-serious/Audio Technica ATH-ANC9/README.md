# Audio Technica ATH-ANC9
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.5; 23 -11.9; 25 -12.3; 28 -12.6; 31 -12.7; 34 -12.5; 37 -12.1; 41 -11.2; 45 -10.1; 49 -9.2; 54 -8.4; 60 -7.8; 66 -7.5; 72 -7.5; 79 -7.8; 87 -8.3; 96 -8.9; 106 -9.1; 116 -9.2; 128 -9.3; 141 -9.0; 155 -8.6; 170 -8.0; 187 -7.2; 206 -6.6; 227 -5.8; 249 -5.3; 274 -4.8; 302 -4.2; 332 -3.7; 365 -3.4; 402 -3.5; 442 -3.1; 486 -3.1; 535 -2.8; 588 -2.1; 647 -1.3; 712 -0.7; 783 -0.5; 861 -1.6; 947 -3.7; 1042 -6.9; 1146 -10.2; 1261 -13.3; 1387 -14.7; 1526 -15.0; 1678 -13.2; 1846 -11.9; 2031 -10.6; 2234 -10.9; 2457 -10.3; 2703 -10.7; 2973 -11.5; 3270 -11.9; 3597 -12.0; 3957 -12.2; 4353 -12.0; 4788 -10.9; 5267 -9.7; 5793 -9.2; 6373 -5.3; 7010 -4.6; 7711 -5.3; 8482 -5.6; 9330 -5.6; 10263 -5.6; 11289 -5.6; 12418 -5.6; 13660 -5.6; 15026 -5.6; 16529 -5.6; 18182 -5.6; 20000 -5.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-ANC9 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-ANC9 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.8dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 29 Hz   | 1    | -7.4 dB  |
| Peaking | 128 Hz  | 1.4  | -3.8 dB  |
| Peaking | 871 Hz  | 0.85 | 11.5 dB  |
| Peaking | 1338 Hz | 1.15 | -15.9 dB |
| Peaking | 3903 Hz | 1.73 | -6.0 dB  |
| Peaking | 334 Hz  | 4.26 | 0.9 dB   |
| Peaking | 2973 Hz | 7.72 | -1.1 dB  |
| Peaking | 5764 Hz | 3.46 | -4.0 dB  |
| Peaking | 6436 Hz | 2.52 | 4.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.1 dB |
| Peaking | 62 Hz    | 1.41 | 0.0 dB  |
| Peaking | 125 Hz   | 1.41 | -3.9 dB |
| Peaking | 250 Hz   | 1.41 | 0.1 dB  |
| Peaking | 500 Hz   | 1.41 | 4.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | -7.1 dB |
| Peaking | 4000 Hz  | 1.41 | -5.6 dB |
| Peaking | 8000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-ANC9/Audio%20Technica%20ATH-ANC9.png)