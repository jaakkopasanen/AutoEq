# Beyerdynamic Xelento
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.1; 23 -13.2; 25 -13.2; 28 -13.3; 31 -13.3; 34 -13.3; 37 -13.3; 41 -13.2; 45 -13.2; 49 -13.2; 54 -13.2; 60 -13.3; 66 -13.3; 72 -13.4; 79 -13.5; 87 -13.6; 96 -13.8; 106 -13.8; 116 -13.8; 128 -13.7; 141 -13.5; 155 -13.4; 170 -13.1; 187 -12.8; 206 -12.4; 227 -11.9; 249 -11.4; 274 -10.9; 302 -10.3; 332 -9.7; 365 -9.0; 402 -8.5; 442 -7.9; 486 -7.3; 535 -6.7; 588 -6.1; 647 -5.5; 712 -5.0; 783 -4.4; 861 -4.1; 947 -4.0; 1042 -4.3; 1146 -4.8; 1261 -5.2; 1387 -5.3; 1526 -5.0; 1678 -4.6; 1846 -4.3; 2031 -3.7; 2234 -3.0; 2457 -2.2; 2703 -1.4; 2973 -0.6; 3270 -0.5; 3597 -0.5; 3957 -1.4; 4353 -3.7; 4788 -7.4; 5267 -7.0; 5793 -1.1; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -7.6; 16529 -11.0; 18182 -11.3; 20000 -8.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic Xelento GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic Xelento ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 75 Hz    | 0.14 | -7.3 dB |
| Peaking | 696 Hz   | 0.7  | 4.2 dB  |
| Peaking | 3115 Hz  | 1.74 | 5.4 dB  |
| Peaking | 9450 Hz  | 0.24 | 1.2 dB  |
| Peaking | 17773 Hz | 0.91 | -6.0 dB |
| Peaking | 14 Hz    | 1.88 | -1.1 dB |
| Peaking | 3972 Hz  | 5.62 | 1.7 dB  |
| Peaking | 5059 Hz  | 4.22 | -7.1 dB |
| Peaking | 6042 Hz  | 2.85 | 7.3 dB  |
| Peaking | 7825 Hz  | 1.92 | -2.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.8 dB |
| Peaking | 62 Hz    | 1.41 | -4.8 dB |
| Peaking | 125 Hz   | 1.41 | -6.1 dB |
| Peaking | 250 Hz   | 1.41 | -4.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -3.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Beyerdynamic%20Xelento/Beyerdynamic%20Xelento.png)