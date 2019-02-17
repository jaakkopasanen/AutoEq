# Beyerdynamic DT 235
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.8; 41 -1.7; 45 -2.6; 49 -3.4; 54 -4.3; 60 -5.0; 66 -5.6; 72 -6.3; 79 -6.8; 87 -6.9; 96 -7.3; 106 -8.0; 116 -8.3; 128 -8.6; 141 -8.7; 155 -8.6; 170 -8.4; 187 -8.1; 206 -7.3; 227 -7.0; 249 -7.1; 274 -7.1; 302 -7.0; 332 -7.1; 365 -7.3; 402 -7.4; 442 -7.0; 486 -7.0; 535 -6.8; 588 -6.4; 647 -6.7; 712 -7.3; 783 -7.5; 861 -7.7; 947 -7.0; 1042 -6.6; 1146 -6.4; 1261 -6.0; 1387 -6.3; 1526 -9.2; 1678 -11.0; 1846 -9.9; 2031 -7.8; 2234 -6.2; 2457 -4.5; 2703 -3.7; 2973 -1.9; 3270 -1.4; 3597 -3.1; 3957 -0.7; 4353 -4.3; 4788 -10.4; 5267 -8.4; 5793 -3.6; 6373 -1.4; 7010 -4.0; 7711 -7.8; 8482 -12.5; 9330 -13.4; 10263 -10.3; 11289 -6.7; 12418 -6.5; 13660 -8.2; 15026 -9.3; 16529 -6.5; 18182 -6.5; 20000 -6.5
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
| Peaking | 29 Hz    | 1.38 | 7.1 dB  |
| Peaking | 1729 Hz  | 4.21 | -5.2 dB |
| Peaking | 3228 Hz  | 2.51 | 5.8 dB  |
| Peaking | 6543 Hz  | 5.71 | 6.5 dB  |
| Peaking | 9031 Hz  | 2.99 | -7.9 dB |
| Peaking | 137 Hz   | 1.51 | -2.5 dB |
| Peaking | 465 Hz   | 0.9  | -0.5 dB |
| Peaking | 4091 Hz  | 8.04 | 4.4 dB  |
| Peaking | 4801 Hz  | 6.98 | -5.7 dB |
| Peaking | 14706 Hz | 5.79 | -3.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.5 dB  |
| Peaking | 62 Hz    | 1.41 | 0.2 dB  |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | -0.3 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB |
| Peaking | 4000 Hz  | 1.41 | 5.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.5 dB |
| Peaking | 16000 Hz | 1.41 | -1.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DT%20235/Beyerdynamic%20DT%20235.png)