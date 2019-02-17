# Grado SR60
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.7; 31 -1.6; 34 -2.5; 37 -3.3; 41 -4.1; 45 -4.9; 49 -5.5; 54 -6.0; 60 -6.7; 66 -6.9; 72 -7.0; 79 -7.5; 87 -7.9; 96 -8.0; 106 -8.0; 116 -8.0; 128 -7.9; 141 -7.6; 155 -7.5; 170 -7.6; 187 -7.4; 206 -7.0; 227 -7.1; 249 -7.9; 274 -7.8; 302 -7.5; 332 -7.1; 365 -6.9; 402 -6.6; 442 -6.5; 486 -6.4; 535 -6.2; 588 -6.2; 647 -6.0; 712 -6.0; 783 -6.1; 861 -6.2; 947 -6.4; 1042 -6.7; 1146 -6.9; 1261 -7.4; 1387 -8.3; 1526 -9.3; 1678 -10.4; 1846 -11.2; 2031 -11.9; 2234 -12.2; 2457 -12.1; 2703 -11.1; 2973 -8.6; 3270 -6.4; 3597 -5.1; 3957 -6.6; 4353 -9.9; 4788 -14.2; 5267 -10.7; 5793 -9.1; 6373 -7.1; 7010 -9.8; 7711 -12.2; 8482 -14.6; 9330 -13.3; 10263 -6.9; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -8.1; 16529 -7.7; 18182 -6.9; 20000 -8.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR60 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR60 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 0.9  | 6.6 dB  |
| Peaking | 90 Hz    | 0.59 | -2.0 dB |
| Peaking | 2161 Hz  | 1.85 | -6.1 dB |
| Peaking | 8437 Hz  | 2.72 | -8.2 dB |
| Peaking | 20516 Hz | 1.95 | -5.9 dB |
| Peaking | 3692 Hz  | 4.15 | 4.3 dB  |
| Peaking | 4742 Hz  | 4.4  | -7.3 dB |
| Peaking | 6368 Hz  | 7.64 | 2.2 dB  |
| Peaking | 10889 Hz | 4.82 | 2.3 dB  |
| Peaking | 15753 Hz | 3.71 | -1.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | -1.5 dB |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.6 dB |
| Peaking | 4000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20SR60/Grado%20SR60.png)