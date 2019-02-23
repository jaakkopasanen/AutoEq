# Skullcandy Venue
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.4; 23 -13.2; 25 -12.9; 28 -12.5; 31 -12.0; 34 -11.5; 37 -11.0; 41 -10.4; 45 -9.8; 49 -9.4; 54 -9.0; 60 -8.6; 66 -8.4; 72 -8.2; 79 -8.0; 87 -8.0; 96 -8.0; 106 -8.1; 116 -8.2; 128 -8.3; 141 -8.3; 155 -8.4; 170 -8.4; 187 -8.3; 206 -8.0; 227 -7.7; 249 -7.3; 274 -6.8; 302 -6.2; 332 -5.5; 365 -4.6; 402 -3.4; 442 -2.5; 486 -2.1; 535 -1.7; 588 -1.3; 647 -1.0; 712 -0.7; 783 -0.5; 861 -0.5; 947 -0.7; 1042 -1.0; 1146 -1.6; 1261 -2.7; 1387 -4.7; 1526 -6.7; 1678 -7.6; 1846 -6.7; 2031 -5.8; 2234 -5.4; 2457 -4.8; 2703 -4.9; 2973 -6.4; 3270 -8.0; 3597 -6.7; 3957 -7.5; 4353 -7.1; 4788 -6.3; 5267 -4.5; 5793 -7.9; 6373 -10.7; 7010 -9.9; 7711 -9.0; 8482 -9.7; 9330 -11.2; 10263 -10.7; 11289 -8.6; 12418 -8.3; 13660 -11.5; 15026 -14.8; 16529 -12.7; 18182 -8.4; 20000 -8.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Venue GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Venue ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 724 Hz   | 1.09 | 6.1 dB  |
| Peaking | 8360 Hz  | 1.06 | -4.1 dB |
| Peaking | 15509 Hz | 1.73 | -8.9 dB |
| Peaking | 20893 Hz | 1.07 | -7.0 dB |
| Peaking | 22 Hz    | 0.77 | -5.8 dB |
| Peaking | 26 Hz    | 0.25 | -1.8 dB |
| Peaking | 180 Hz   | 1.13 | -2.6 dB |
| Peaking | 5117 Hz  | 1.52 | -2.3 dB |
| Peaking | 5250 Hz  | 5.44 | 5.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.3 dB |
| Peaking | 62 Hz    | 1.41 | -0.9 dB |
| Peaking | 125 Hz   | 1.41 | -2.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | 4.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB |
| Peaking | 4000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.3 dB |
| Peaking | 16000 Hz | 1.41 | -9.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Skullcandy%20Venue/Skullcandy%20Venue.png)