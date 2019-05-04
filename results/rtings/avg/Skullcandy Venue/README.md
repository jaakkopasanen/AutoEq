# Skullcandy Venue
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.1; 23 -12.9; 25 -12.6; 28 -12.2; 31 -11.7; 34 -11.2; 37 -10.7; 41 -10.1; 45 -9.5; 49 -9.1; 54 -8.7; 60 -8.3; 66 -8.1; 72 -7.8; 79 -7.7; 87 -7.6; 96 -7.7; 106 -7.7; 116 -7.8; 128 -7.9; 141 -8.0; 155 -8.0; 170 -8.1; 187 -8.0; 206 -7.7; 227 -7.4; 249 -7.1; 274 -6.7; 302 -6.1; 332 -5.4; 365 -4.4; 402 -3.3; 442 -2.4; 486 -2.0; 535 -1.7; 588 -1.3; 647 -1.0; 712 -0.7; 783 -0.5; 861 -0.5; 947 -0.7; 1042 -1.0; 1146 -1.6; 1261 -2.8; 1387 -4.8; 1526 -6.8; 1678 -7.7; 1846 -6.9; 2031 -6.2; 2234 -6.1; 2457 -5.6; 2703 -5.4; 2973 -6.4; 3270 -7.5; 3597 -6.5; 3957 -6.9; 4353 -6.7; 4788 -6.5; 5267 -5.0; 5793 -7.6; 6373 -9.6; 7010 -9.9; 7711 -9.6; 8482 -9.2; 9330 -9.3; 10263 -10.1; 11289 -9.6; 12418 -8.4; 13660 -10.6; 15026 -14.1; 16529 -12.5; 18182 -8.1; 20000 -8.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Venue GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Venue ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 724 Hz   |  1.16 | 5.9 dB  |
| Peaking | 8275 Hz  |  0.89 | -3.6 dB |
| Peaking | 15598 Hz |  1.68 | -8.4 dB |
| Peaking | 20731 Hz |  1.34 | -6.0 dB |
| Peaking | 21 Hz    |  0.74 | -5.9 dB |
| Peaking | 28 Hz    |  0.3  | -1.5 dB |
| Peaking | 183 Hz   |  1.26 | -2.4 dB |
| Peaking | 1674 Hz  |  5.1  | -3.2 dB |
| Peaking | 5263 Hz  | 10.26 | 3.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.1 dB |
| Peaking | 62 Hz    | 1.41 | -0.7 dB |
| Peaking | 125 Hz   | 1.41 | -1.9 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | 4.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.3 dB |
| Peaking | 4000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.1 dB |
| Peaking | 16000 Hz | 1.41 | -8.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Skullcandy%20Venue/Skullcandy%20Venue.png)