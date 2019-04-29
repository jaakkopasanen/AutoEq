# Vision Ears VE8
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.6; 23 -3.8; 25 -4.0; 28 -4.3; 31 -4.5; 34 -4.6; 37 -4.8; 41 -5.1; 45 -5.3; 49 -5.5; 54 -5.7; 60 -5.9; 66 -6.3; 72 -6.6; 79 -7.0; 87 -7.3; 96 -7.7; 106 -8.1; 116 -8.4; 128 -8.7; 141 -8.9; 155 -9.1; 170 -9.1; 187 -9.1; 206 -9.1; 227 -8.9; 249 -8.8; 274 -8.6; 302 -8.3; 332 -8.0; 365 -7.7; 402 -7.4; 442 -7.0; 486 -6.7; 535 -6.2; 588 -5.8; 647 -5.3; 712 -4.8; 783 -4.3; 861 -3.9; 947 -3.7; 1042 -4.0; 1146 -4.8; 1261 -5.6; 1387 -6.1; 1526 -6.1; 1678 -5.5; 1846 -4.5; 2031 -3.5; 2234 -3.0; 2457 -2.9; 2703 -2.8; 2973 -2.7; 3270 -2.3; 3597 -1.6; 3957 -0.9; 4353 -0.5; 4788 -0.6; 5267 -1.3; 5793 -3.1; 6373 -3.6; 7010 -4.9; 7711 -7.3; 8482 -7.3; 9330 -5.6; 10263 -5.5; 11289 -5.5; 12418 -5.5; 13660 -5.5; 15026 -5.5; 16529 -5.5; 18182 -5.6; 20000 -10.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Vision Ears VE8 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Vision Ears VE8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 12 Hz    | 0.28 | 2.2 dB  |
| Peaking | 179 Hz   | 0.53 | -3.8 dB |
| Peaking | 848 Hz   | 2.52 | 2.2 dB  |
| Peaking | 4332 Hz  | 1    | 5.1 dB  |
| Peaking | 7973 Hz  | 3.26 | -3.7 dB |
| Peaking | 1050 Hz  | 5.24 | 0.9 dB  |
| Peaking | 1517 Hz  | 2.14 | -2.2 dB |
| Peaking | 2112 Hz  | 1.34 | 1.6 dB  |
| Peaking | 3216 Hz  | 3.06 | -1.0 dB |
| Peaking | 20058 Hz | 2.26 | -4.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.6 dB  |
| Peaking | 62 Hz    | 1.41 | -0.4 dB |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | -3.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.1 dB |
| Peaking | 4000 Hz  | 1.41 | 5.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Vision%20Ears%20VE8/Vision%20Ears%20VE8.png)