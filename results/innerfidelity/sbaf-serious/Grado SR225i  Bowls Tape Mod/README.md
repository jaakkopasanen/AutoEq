# Grado SR225i  Bowls Tape Mod
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.8; 45 -1.7; 49 -2.6; 54 -3.5; 60 -4.3; 66 -5.0; 72 -5.6; 79 -6.4; 87 -7.0; 96 -7.4; 106 -7.6; 116 -7.6; 128 -7.7; 141 -7.7; 155 -7.6; 170 -7.4; 187 -7.1; 206 -7.0; 227 -6.7; 249 -6.4; 274 -6.0; 302 -6.0; 332 -6.0; 365 -5.6; 402 -5.6; 442 -5.3; 486 -5.3; 535 -5.1; 588 -4.8; 647 -4.6; 712 -4.7; 783 -4.6; 861 -4.8; 947 -4.9; 1042 -5.0; 1146 -4.9; 1261 -5.4; 1387 -5.9; 1526 -6.6; 1678 -6.6; 1846 -8.0; 2031 -9.7; 2234 -6.6; 2457 -4.6; 2703 -3.6; 2973 -4.8; 3270 -4.5; 3597 -6.5; 3957 -6.2; 4353 -5.0; 4788 -5.2; 5267 -6.6; 5793 -5.7; 6373 -7.0; 7010 -11.0; 7711 -11.0; 8482 -11.4; 9330 -11.7; 10263 -6.8; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR225i  Bowls Tape Mod GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR225i  Bowls Tape Mod ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 30 Hz    | 1.19 | 7.1 dB  |
| Peaking | 724 Hz   | 1.2  | 1.9 dB  |
| Peaking | 2027 Hz  | 3.77 | -6.7 dB |
| Peaking | 2397 Hz  | 1.44 | 4.1 dB  |
| Peaking | 8289 Hz  | 2.6  | -5.9 dB |
| Peaking | 49 Hz    | 2.53 | 1.5 dB  |
| Peaking | 118 Hz   | 1.24 | -1.8 dB |
| Peaking | 3767 Hz  | 5.89 | -1.6 dB |
| Peaking | 4533 Hz  | 4.05 | 1.6 dB  |
| Peaking | 10853 Hz | 6.84 | 1.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.6 dB  |
| Peaking | 62 Hz    | 1.41 | 0.7 dB  |
| Peaking | 125 Hz   | 1.41 | -2.0 dB |
| Peaking | 250 Hz   | 1.41 | 0.0 dB  |
| Peaking | 500 Hz   | 1.41 | 1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.4 dB |
| Peaking | 4000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20SR225i%20%20Bowls%20Tape%20Mod/Grado%20SR225i%20%20Bowls%20Tape%20Mod.png)