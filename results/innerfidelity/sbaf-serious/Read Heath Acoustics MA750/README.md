# Read Heath Acoustics MA750
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.0; 23 -11.0; 25 -11.0; 28 -11.0; 31 -11.0; 34 -11.1; 37 -11.1; 41 -11.0; 45 -11.0; 49 -11.0; 54 -11.0; 60 -11.1; 66 -11.2; 72 -11.3; 79 -11.4; 87 -11.5; 96 -11.7; 106 -11.7; 116 -11.6; 128 -11.7; 141 -11.8; 155 -11.7; 170 -11.6; 187 -11.5; 206 -11.3; 227 -11.0; 249 -10.8; 274 -10.5; 302 -10.2; 332 -9.8; 365 -9.4; 402 -8.9; 442 -8.3; 486 -8.1; 535 -7.6; 588 -6.7; 647 -6.3; 712 -5.9; 783 -5.4; 861 -5.3; 947 -5.1; 1042 -5.1; 1146 -4.9; 1261 -4.8; 1387 -4.8; 1526 -5.2; 1678 -5.2; 1846 -4.8; 2031 -4.4; 2234 -4.1; 2457 -3.7; 2703 -3.9; 2973 -4.3; 3270 -5.3; 3597 -6.6; 3957 -8.3; 4353 -11.6; 4788 -13.0; 5267 -9.4; 5793 -4.0; 6373 -0.5; 7010 -2.6; 7711 -4.8; 8482 -5.1; 9330 -5.1; 10263 -5.1; 11289 -5.3; 12418 -5.1; 13660 -6.0; 15026 -9.7; 16529 -5.8; 18182 -5.1; 20000 -5.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Read Heath Acoustics MA750 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Read Heath Acoustics MA750 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 38 Hz    | 0.18 | -5.9 dB |
| Peaking | 227 Hz   | 0.69 | -3.5 dB |
| Peaking | 4704 Hz  | 4.14 | -9.4 dB |
| Peaking | 6388 Hz  | 4.63 | 6.1 dB  |
| Peaking | 15002 Hz | 3.91 | -5.1 dB |
| Peaking | 473 Hz   | 1.88 | -0.9 dB |
| Peaking | 845 Hz   | 1.01 | 0.8 dB  |
| Peaking | 2611 Hz  | 2.41 | 1.8 dB  |
| Peaking | 4076 Hz  | 4.7  | -1.0 dB |
| Peaking | 20594 Hz | 3.86 | 0.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.0 dB |
| Peaking | 62 Hz    | 1.41 | -4.2 dB |
| Peaking | 125 Hz   | 1.41 | -5.4 dB |
| Peaking | 250 Hz   | 1.41 | -4.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.7 dB |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 4000 Hz  | 1.41 | -4.5 dB |
| Peaking | 8000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 16000 Hz | 1.41 | -2.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Read%20Heath%20Acoustics%20MA750/Read%20Heath%20Acoustics%20MA750.png)