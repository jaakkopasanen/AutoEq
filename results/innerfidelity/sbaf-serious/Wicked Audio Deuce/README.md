# Wicked Audio Deuce
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.9; 23 -14.8; 25 -14.7; 28 -14.5; 31 -14.4; 34 -14.2; 37 -14.1; 41 -13.9; 45 -13.7; 49 -13.5; 54 -13.3; 60 -13.2; 66 -13.0; 72 -12.9; 79 -12.8; 87 -12.7; 96 -12.5; 106 -12.2; 116 -11.9; 128 -11.6; 141 -11.2; 155 -10.8; 170 -10.3; 187 -9.8; 206 -9.2; 227 -8.6; 249 -8.0; 274 -7.4; 302 -6.7; 332 -6.1; 365 -5.3; 402 -4.7; 442 -3.9; 486 -3.4; 535 -2.8; 588 -2.0; 647 -1.5; 712 -1.3; 783 -1.1; 861 -0.5; 947 -0.8; 1042 -1.1; 1146 -1.3; 1261 -1.9; 1387 -2.1; 1526 -3.2; 1678 -4.3; 1846 -5.4; 2031 -6.1; 2234 -6.6; 2457 -6.5; 2703 -6.1; 2973 -4.2; 3270 -2.2; 3597 -0.6; 3957 -1.3; 4353 -3.6; 4788 -5.7; 5267 -8.2; 5793 -13.6; 6373 -9.1; 7010 -4.8; 7711 -5.3; 8482 -6.2; 9330 -7.3; 10263 -5.6; 11289 -5.6; 12418 -5.6; 13660 -5.6; 15026 -5.6; 16529 -5.6; 18182 -5.6; 20000 -5.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Wicked Audio Deuce GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Wicked Audio Deuce ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.25 | -9.0 dB |
| Peaking | 131 Hz  | 0.66 | -3.7 dB |
| Peaking | 800 Hz  | 0.96 | 5.5 dB  |
| Peaking | 3729 Hz | 4.44 | 5.6 dB  |
| Peaking | 5835 Hz | 6.56 | -9.2 dB |
| Peaking | 769 Hz  | 4.14 | -1.1 dB |
| Peaking | 1347 Hz | 3.42 | 1.0 dB  |
| Peaking | 2232 Hz | 2.21 | -2.9 dB |
| Peaking | 2587 Hz | 0.23 | 0.6 dB  |
| Peaking | 9191 Hz | 7.72 | -2.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -9.4 dB |
| Peaking | 62 Hz    | 1.41 | -5.4 dB |
| Peaking | 125 Hz   | 1.41 | -5.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | 2.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.6 dB |
| Peaking | 4000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Wicked%20Audio%20Deuce/Wicked%20Audio%20Deuce.png)