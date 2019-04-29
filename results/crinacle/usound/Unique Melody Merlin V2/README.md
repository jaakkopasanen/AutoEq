# Unique Melody Merlin V2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.5; 23 -4.6; 25 -4.7; 28 -4.9; 31 -5.0; 34 -5.2; 37 -5.3; 41 -5.5; 45 -5.7; 49 -5.9; 54 -6.1; 60 -6.3; 66 -6.7; 72 -7.0; 79 -7.3; 87 -7.7; 96 -8.2; 106 -8.6; 116 -8.9; 128 -9.2; 141 -9.5; 155 -9.7; 170 -9.8; 187 -9.9; 206 -9.9; 227 -9.8; 249 -9.7; 274 -9.6; 302 -9.4; 332 -9.2; 365 -9.0; 402 -8.7; 442 -8.5; 486 -8.1; 535 -7.8; 588 -7.3; 647 -6.9; 712 -6.4; 783 -5.9; 861 -5.4; 947 -5.2; 1042 -5.2; 1146 -5.7; 1261 -6.3; 1387 -6.6; 1526 -6.4; 1678 -5.9; 1846 -5.2; 2031 -4.3; 2234 -3.4; 2457 -2.5; 2703 -1.8; 2973 -1.7; 3270 -1.8; 3597 -1.2; 3957 -1.1; 4353 -2.0; 4788 -1.6; 5267 -0.5; 5793 -1.0; 6373 -3.8; 7010 -3.4; 7711 -5.6; 8482 -5.8; 9330 -5.9; 10263 -7.7; 11289 -8.0; 12418 -6.6; 13660 -8.4; 15026 -7.7; 16529 -5.9; 18182 -5.9; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Unique Melody Merlin V2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Unique Melody Merlin V2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 37 Hz    | 0.36 | 1.8 dB  |
| Peaking | 186 Hz   | 0.36 | -4.4 dB |
| Peaking | 850 Hz   | 3.05 | 1.5 dB  |
| Peaking | 4502 Hz  | 0.74 | 5.6 dB  |
| Peaking | 11155 Hz | 0.77 | -3.0 dB |
| Peaking | 1533 Hz  | 3.47 | -1.5 dB |
| Peaking | 2636 Hz  | 3.59 | 1.2 dB  |
| Peaking | 4455 Hz  | 6.08 | -1.4 dB |
| Peaking | 5484 Hz  | 9.25 | 1.7 dB  |
| Peaking | 16524 Hz | 5    | 0.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.3 dB  |
| Peaking | 62 Hz    | 1.41 | -0.2 dB |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | -3.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.6 dB |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -1.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Unique%20Melody%20Merlin%20V2/Unique%20Melody%20Merlin%20V2.png)