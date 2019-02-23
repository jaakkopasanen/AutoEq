# Beyerdynamic DT 235
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.6; 41 -1.4; 45 -2.3; 49 -3.1; 54 -3.9; 60 -4.7; 66 -5.3; 72 -6.0; 79 -6.5; 87 -6.5; 96 -6.9; 106 -7.6; 116 -7.9; 128 -8.2; 141 -8.3; 155 -8.3; 170 -8.0; 187 -7.7; 206 -6.9; 227 -6.7; 249 -6.7; 274 -6.7; 302 -6.6; 332 -6.8; 365 -6.9; 402 -7.0; 442 -6.6; 486 -6.6; 535 -6.5; 588 -6.1; 647 -6.3; 712 -6.9; 783 -7.1; 861 -7.3; 947 -6.6; 1042 -6.3; 1146 -6.0; 1261 -5.6; 1387 -5.9; 1526 -8.8; 1678 -10.6; 1846 -9.6; 2031 -7.5; 2234 -5.8; 2457 -4.1; 2703 -3.3; 2973 -1.5; 3270 -1.0; 3597 -2.7; 3957 -0.6; 4353 -3.9; 4788 -10.0; 5267 -8.1; 5793 -3.2; 6373 -1.2; 7010 -4.0; 7711 -7.5; 8482 -12.1; 9330 -13.0; 10263 -9.9; 11289 -6.6; 12418 -6.5; 13660 -7.9; 15026 -9.0; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 235 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 235 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 29 Hz    | 1.25 | 7.1 dB  |
| Peaking | 1730 Hz  | 4.73 | -5.0 dB |
| Peaking | 3224 Hz  | 2.39 | 6.1 dB  |
| Peaking | 6496 Hz  | 5.78 | 6.4 dB  |
| Peaking | 9038 Hz  | 3.22 | -7.6 dB |
| Peaking | 138 Hz   | 1.66 | -2.2 dB |
| Peaking | 4138 Hz  | 7.47 | 5.0 dB  |
| Peaking | 4822 Hz  | 4.79 | -5.5 dB |
| Peaking | 5910 Hz  | 9.73 | 2.6 dB  |
| Peaking | 14554 Hz | 6.02 | -3.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.5 dB  |
| Peaking | 62 Hz    | 1.41 | 0.6 dB  |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | -0.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB |
| Peaking | 4000 Hz  | 1.41 | 5.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.2 dB |
| Peaking | 16000 Hz | 1.41 | -1.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DT%20235/Beyerdynamic%20DT%20235.png)