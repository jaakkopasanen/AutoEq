# Spiral Ears SE5U
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.4; 23 -2.1; 25 -2.8; 28 -3.6; 31 -4.2; 34 -4.7; 37 -5.1; 41 -5.6; 45 -6.1; 49 -6.5; 54 -7.0; 60 -7.5; 66 -7.9; 72 -8.3; 79 -8.8; 87 -9.2; 96 -9.7; 106 -10.2; 116 -10.5; 128 -10.7; 141 -10.9; 155 -11.0; 170 -11.1; 187 -11.1; 206 -11.0; 227 -10.8; 249 -10.6; 274 -10.3; 302 -10.0; 332 -9.6; 365 -9.2; 402 -8.8; 442 -8.4; 486 -7.9; 535 -7.4; 588 -7.0; 647 -6.5; 712 -6.0; 783 -5.5; 861 -5.2; 947 -5.2; 1042 -5.7; 1146 -6.8; 1261 -8.1; 1387 -9.5; 1526 -10.8; 1678 -12.3; 1846 -13.0; 2031 -12.3; 2234 -10.0; 2457 -8.1; 2703 -7.5; 2973 -8.2; 3270 -2.9; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -8.0; 13660 -10.2; 15026 -11.6; 16529 -10.5; 18182 -6.7; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Spiral Ears SE5U GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Spiral Ears SE5U ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 19 Hz    | 1    | 5.5 dB  |
| Peaking | 165 Hz   | 0.65 | -5.0 dB |
| Peaking | 1900 Hz  | 2.23 | -7.8 dB |
| Peaking | 4668 Hz  | 1.26 | 7.4 dB  |
| Peaking | 15161 Hz | 1.48 | -5.6 dB |
| Peaking | 879 Hz   | 2.81 | 2.4 dB  |
| Peaking | 3050 Hz  | 5.75 | -4.2 dB |
| Peaking | 3420 Hz  | 6.56 | 4.2 dB  |
| Peaking | 6496 Hz  | 5.18 | 3.3 dB  |
| Peaking | 7331 Hz  | 2.34 | -2.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.6 dB  |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | -3.8 dB |
| Peaking | 250 Hz   | 1.41 | -3.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -8.5 dB |
| Peaking | 4000 Hz  | 1.41 | 8.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -5.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Spiral%20Ears%20SE5U/Spiral%20Ears%20SE5U.png)