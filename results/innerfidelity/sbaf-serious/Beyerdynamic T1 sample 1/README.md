# Beyerdynamic T1 sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.8; 25 -1.2; 28 -1.8; 31 -2.2; 34 -2.6; 37 -3.0; 41 -3.3; 45 -3.7; 49 -4.0; 54 -3.9; 60 -3.5; 66 -4.5; 72 -5.3; 79 -5.9; 87 -6.4; 96 -6.9; 106 -7.2; 116 -7.5; 128 -7.8; 141 -8.1; 155 -8.3; 170 -8.4; 187 -8.5; 206 -8.6; 227 -8.6; 249 -8.6; 274 -8.5; 302 -8.5; 332 -8.3; 365 -8.2; 402 -8.0; 442 -7.8; 486 -7.6; 535 -7.5; 588 -7.2; 647 -7.0; 712 -7.1; 783 -6.6; 861 -6.6; 947 -6.4; 1042 -6.3; 1146 -6.0; 1261 -5.8; 1387 -5.9; 1526 -7.0; 1678 -8.0; 1846 -8.2; 2031 -6.4; 2234 -4.7; 2457 -6.8; 2703 -6.1; 2973 -5.9; 3270 -5.0; 3597 -5.4; 3957 -5.5; 4353 -6.4; 4788 -2.7; 5267 -0.9; 5793 -9.6; 6373 -11.7; 7010 -8.6; 7711 -14.1; 8482 -18.7; 9330 -17.1; 10263 -9.8; 11289 -6.4; 12418 -6.4; 13660 -6.6; 15026 -8.2; 16529 -8.4; 18182 -6.5; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic T1 sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T1 sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 18 Hz    |  0.59 | 6.0 dB   |
| Peaking | 59 Hz    |  3.38 | 1.7 dB   |
| Peaking | 204 Hz   |  0.57 | -2.5 dB  |
| Peaking | 5092 Hz  |  8.76 | 7.9 dB   |
| Peaking | 8630 Hz  |  3.2  | -13.6 dB |
| Peaking | 1765 Hz  |  5.48 | -3.1 dB  |
| Peaking | 2535 Hz  |  0.57 | 1.1 dB   |
| Peaking | 6100 Hz  | 10.93 | -5.8 dB  |
| Peaking | 11402 Hz |  4.7  | 2.7 dB   |
| Peaking | 16195 Hz |  2.71 | -2.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.0 dB  |
| Peaking | 62 Hz    | 1.41 | 1.4 dB  |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB |
| Peaking | 4000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -9.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20T1%20sample%201/Beyerdynamic%20T1%20sample%201.png)