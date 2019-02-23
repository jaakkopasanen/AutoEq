# Read Heath Acoustics MA750
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.0; 23 -10.0; 25 -10.0; 28 -10.0; 31 -10.1; 34 -10.1; 37 -10.1; 41 -10.1; 45 -10.0; 49 -10.0; 54 -10.0; 60 -10.1; 66 -10.2; 72 -10.3; 79 -10.4; 87 -10.5; 96 -10.7; 106 -10.7; 116 -10.7; 128 -10.7; 141 -10.8; 155 -10.7; 170 -10.6; 187 -10.5; 206 -10.3; 227 -10.0; 249 -9.8; 274 -9.5; 302 -9.2; 332 -8.8; 365 -8.4; 402 -7.9; 442 -7.4; 486 -7.1; 535 -6.6; 588 -5.8; 647 -5.3; 712 -4.9; 783 -4.4; 861 -4.3; 947 -4.1; 1042 -4.1; 1146 -3.9; 1261 -3.9; 1387 -3.9; 1526 -4.2; 1678 -4.2; 1846 -3.9; 2031 -3.5; 2234 -3.1; 2457 -2.7; 2703 -3.0; 2973 -3.3; 3270 -4.3; 3597 -5.6; 3957 -7.3; 4353 -10.6; 4788 -12.0; 5267 -8.4; 5793 -3.0; 6373 -0.5; 7010 -3.4; 7711 -5.6; 8482 -5.9; 9330 -5.9; 10263 -5.9; 11289 -5.9; 12418 -5.9; 13660 -6.0; 15026 -8.7; 16529 -6.0; 18182 -5.9; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Read Heath Acoustics MA750 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Read Heath Acoustics MA750 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 16 Hz    | 0.23 | -3.8 dB |
| Peaking | 180 Hz   | 0.43 | -4.4 dB |
| Peaking | 1683 Hz  | 0.35 | 3.0 dB  |
| Peaking | 4691 Hz  | 3.56 | -8.9 dB |
| Peaking | 6227 Hz  | 5.16 | 6.4 dB  |
| Peaking | 761 Hz   | 2.3  | 0.6 dB  |
| Peaking | 1656 Hz  | 3.38 | -0.9 dB |
| Peaking | 2664 Hz  | 2.47 | 1.3 dB  |
| Peaking | 3016 Hz  | 0.14 | -0.2 dB |
| Peaking | 15047 Hz | 4.87 | -3.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.1 dB |
| Peaking | 62 Hz    | 1.41 | -3.0 dB |
| Peaking | 125 Hz   | 1.41 | -4.0 dB |
| Peaking | 250 Hz   | 1.41 | -3.5 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.5 dB |
| Peaking | 8000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 16000 Hz | 1.41 | -1.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Read%20Heath%20Acoustics%20MA750/Read%20Heath%20Acoustics%20MA750.png)