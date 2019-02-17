# Wicked Audio Deuce
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.9; 23 -14.8; 25 -14.7; 28 -14.5; 31 -14.4; 34 -14.2; 37 -14.1; 41 -13.9; 45 -13.7; 49 -13.5; 54 -13.3; 60 -13.2; 66 -13.0; 72 -12.9; 79 -12.8; 87 -12.7; 96 -12.5; 106 -12.2; 116 -11.9; 128 -11.6; 141 -11.2; 155 -10.8; 170 -10.3; 187 -9.8; 206 -9.2; 227 -8.6; 249 -8.0; 274 -7.4; 302 -6.7; 332 -6.1; 365 -5.3; 402 -4.7; 442 -3.9; 486 -3.4; 535 -2.8; 588 -2.0; 647 -1.5; 712 -1.3; 783 -1.1; 861 -0.5; 947 -0.8; 1042 -1.1; 1146 -1.3; 1261 -1.9; 1387 -2.1; 1526 -3.2; 1678 -4.3; 1846 -5.4; 2031 -6.1; 2234 -6.6; 2457 -6.5; 2703 -6.1; 2973 -4.2; 3270 -2.2; 3597 -0.6; 3957 -1.3; 4353 -3.6; 4788 -5.7; 5267 -8.2; 5793 -13.6; 6373 -9.1; 7010 -4.8; 7711 -3.9; 8482 -6.2; 9330 -7.3; 10263 -3.6; 11289 -1.0; 12418 -1.0; 13660 -1.0; 15026 -1.0; 16529 -1.0; 18182 -1.0; 20000 -1.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Wicked Audio Deuce GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Wicked Audio Deuce ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 21 Hz    | 0.17 | -13.5 dB |
| Peaking | 171 Hz   | 0.67 | -4.5 dB  |
| Peaking | 2226 Hz  | 2.38 | -5.9 dB  |
| Peaking | 5900 Hz  | 3.09 | -12.0 dB |
| Peaking | 21330 Hz | 2.3  | -3.6 dB  |
| Peaking | 849 Hz   | 1    | 2.8 dB   |
| Peaking | 994 Hz   | 0.32 | -1.5 dB  |
| Peaking | 3704 Hz  | 4.87 | 3.3 dB   |
| Peaking | 6961 Hz  | 4.82 | 2.1 dB   |
| Peaking | 9084 Hz  | 4.68 | -5.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -14.3 dB |
| Peaking | 62 Hz    | 1.41 | -8.2 dB  |
| Peaking | 125 Hz   | 1.41 | -8.5 dB  |
| Peaking | 250 Hz   | 1.41 | -5.5 dB  |
| Peaking | 500 Hz   | 1.41 | -0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB   |
| Peaking | 2000 Hz  | 1.41 | -5.0 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.5 dB  |
| Peaking | 16000 Hz | 1.41 | 1.0 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Wicked%20Audio%20Deuce/Wicked%20Audio%20Deuce.png)