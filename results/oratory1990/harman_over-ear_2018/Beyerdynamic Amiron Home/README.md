# Beyerdynamic Amiron Home
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.6; 23 -3.0; 25 -3.5; 28 -4.1; 31 -4.6; 34 -5.1; 37 -5.4; 41 -5.8; 45 -6.0; 49 -6.2; 54 -6.4; 60 -6.1; 66 -5.6; 72 -6.2; 79 -7.7; 87 -8.7; 96 -9.3; 106 -9.8; 116 -10.2; 128 -10.6; 141 -10.7; 155 -10.9; 170 -10.9; 187 -10.8; 206 -10.8; 227 -10.7; 249 -10.4; 274 -10.0; 302 -9.5; 332 -9.0; 365 -8.4; 402 -7.8; 442 -7.3; 486 -6.7; 535 -5.9; 588 -5.3; 647 -4.5; 712 -3.8; 783 -3.1; 861 -2.4; 947 -1.7; 1042 -1.3; 1146 -1.0; 1261 -0.8; 1387 -0.8; 1526 -0.7; 1678 -0.5; 1846 -0.5; 2031 -1.1; 2234 -1.2; 2457 -2.2; 2703 -3.6; 2973 -4.6; 3270 -4.8; 3597 -3.8; 3957 -1.7; 4353 -2.5; 4788 -5.6; 5267 -7.1; 5793 -6.5; 6373 -4.6; 7010 -10.1; 7711 -13.5; 8482 -11.2; 9330 -6.1; 10263 -5.9; 11289 -6.0; 12418 -7.7; 13660 -7.4; 15026 -5.9; 16529 -5.9; 18182 -7.2; 20000 -13.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic Amiron Home GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic Amiron Home ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 183 Hz   | 0.55 | -5.6 dB |
| Peaking | 1366 Hz  | 0.7  | 6.0 dB  |
| Peaking | 4089 Hz  | 8.36 | 3.9 dB  |
| Peaking | 7776 Hz  | 4.63 | -8.8 dB |
| Peaking | 18 Hz    | 1.02 | 3.8 dB  |
| Peaking | 68 Hz    | 4.62 | 2.2 dB  |
| Peaking | 5247 Hz  | 8.77 | -1.7 dB |
| Peaking | 19798 Hz | 1.64 | -6.0 dB |
| Peaking | 20199 Hz | 2.26 | -1.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.8 dB  |
| Peaking | 62 Hz    | 1.41 | 0.2 dB  |
| Peaking | 125 Hz   | 1.41 | -4.4 dB |
| Peaking | 250 Hz   | 1.41 | -4.3 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Beyerdynamic%20Amiron%20Home/Beyerdynamic%20Amiron%20Home.png)