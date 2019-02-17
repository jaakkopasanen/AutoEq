# Grado SR225i  Bowls Tape Mod
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -1.0; 41 -2.1; 45 -3.2; 49 -4.2; 54 -5.1; 60 -5.9; 66 -6.6; 72 -7.2; 79 -7.9; 87 -8.5; 96 -8.9; 106 -9.1; 116 -9.2; 128 -9.3; 141 -9.2; 155 -9.1; 170 -8.9; 187 -8.7; 206 -8.5; 227 -8.2; 249 -8.0; 274 -7.6; 302 -7.6; 332 -7.5; 365 -7.2; 402 -7.2; 442 -6.9; 486 -6.9; 535 -6.7; 588 -6.3; 647 -6.2; 712 -6.3; 783 -6.1; 861 -6.4; 947 -6.4; 1042 -6.6; 1146 -6.5; 1261 -6.9; 1387 -7.5; 1526 -8.1; 1678 -8.1; 1846 -9.5; 2031 -11.3; 2234 -8.1; 2457 -6.1; 2703 -5.1; 2973 -6.4; 3270 -6.0; 3597 -8.1; 3957 -7.8; 4353 -6.6; 4788 -6.8; 5267 -8.2; 5793 -7.2; 6373 -8.6; 7010 -12.6; 7711 -12.6; 8482 -12.9; 9330 -13.2; 10263 -7.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR225i  Bowls Tape Mod GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR225i  Bowls Tape Mod ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 29 Hz    | 0.68 | 7.1 dB  |
| Peaking | 106 Hz   | 0.61 | -3.9 dB |
| Peaking | 1980 Hz  | 6.13 | -4.9 dB |
| Peaking | 8619 Hz  | 1.83 | -8.2 dB |
| Peaking | 10945 Hz | 2.58 | 3.3 dB  |
| Peaking | 726 Hz   | 1.97 | 0.6 dB  |
| Peaking | 1527 Hz  | 4.82 | -1.2 dB |
| Peaking | 2655 Hz  | 6.13 | 1.9 dB  |
| Peaking | 6768 Hz  | 2.64 | 1.9 dB  |
| Peaking | 6980 Hz  | 7.11 | -4.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.6 dB  |
| Peaking | 62 Hz    | 1.41 | -0.8 dB |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.5 dB |
| Peaking | 4000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.9 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20SR225i%20%20Bowls%20Tape%20Mod/Grado%20SR225i%20%20Bowls%20Tape%20Mod.png)