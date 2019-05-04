# Beyerdynamic Xelento
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.4; 23 -13.3; 25 -13.2; 28 -13.2; 31 -13.1; 34 -13.0; 37 -12.9; 41 -12.7; 45 -12.6; 49 -12.4; 54 -12.3; 60 -12.2; 66 -12.1; 72 -12.0; 79 -11.9; 87 -11.7; 96 -11.7; 106 -11.7; 116 -11.6; 128 -11.4; 141 -11.1; 155 -11.0; 170 -11.4; 187 -11.5; 206 -11.0; 227 -10.4; 249 -9.9; 274 -9.4; 302 -8.8; 332 -8.3; 365 -8.0; 402 -7.7; 442 -7.2; 486 -6.8; 535 -6.4; 588 -6.1; 647 -5.8; 712 -5.5; 783 -5.1; 861 -5.1; 947 -5.3; 1042 -5.5; 1146 -5.8; 1261 -6.1; 1387 -6.0; 1526 -5.6; 1678 -5.0; 1846 -4.4; 2031 -3.7; 2234 -2.8; 2457 -2.1; 2703 -1.4; 2973 -0.9; 3270 -0.5; 3597 -0.5; 3957 -1.2; 4353 -2.7; 4788 -5.5; 5267 -7.4; 5793 -2.1; 6373 -0.6; 7010 -3.5; 7711 -5.8; 8482 -6.4; 9330 -8.7; 10263 -8.6; 11289 -7.3; 12418 -6.6; 13660 -8.1; 15026 -11.6; 16529 -12.5; 18182 -9.0; 20000 -6.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic Xelento GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic Xelento ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 0.46 | -6.7 dB |
| Peaking | 92 Hz    | 0.61 | -3.6 dB |
| Peaking | 205 Hz   | 1.22 | -3.0 dB |
| Peaking | 3218 Hz  | 1.22 | 5.7 dB  |
| Peaking | 16250 Hz | 1.36 | -7.0 dB |
| Peaking | 790 Hz   | 3.77 | 1.1 dB  |
| Peaking | 5249 Hz  | 5.57 | -5.7 dB |
| Peaking | 6169 Hz  | 3.91 | 6.2 dB  |
| Peaking | 9707 Hz  | 3.03 | -3.0 dB |
| Peaking | 12582 Hz | 3.87 | 1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.5 dB |
| Peaking | 62 Hz    | 1.41 | -4.2 dB |
| Peaking | 125 Hz   | 1.41 | -4.4 dB |
| Peaking | 250 Hz   | 1.41 | -3.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -7.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Beyerdynamic%20Xelento/Beyerdynamic%20Xelento.png)