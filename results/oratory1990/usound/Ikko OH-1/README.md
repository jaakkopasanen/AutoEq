# Ikko OH-1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.4; 23 -4.5; 25 -4.6; 28 -4.7; 31 -4.8; 34 -4.8; 37 -4.9; 41 -5.0; 45 -5.0; 49 -5.1; 54 -5.1; 60 -5.2; 66 -5.3; 72 -5.4; 79 -5.5; 87 -5.5; 96 -5.6; 106 -5.5; 116 -5.4; 128 -5.3; 141 -5.2; 155 -5.2; 170 -5.1; 187 -4.9; 206 -4.6; 227 -4.2; 249 -3.9; 274 -3.6; 302 -3.2; 332 -2.8; 365 -2.5; 402 -2.2; 442 -2.0; 486 -1.8; 535 -1.5; 588 -1.3; 647 -1.1; 712 -0.9; 783 -0.6; 861 -0.5; 947 -0.6; 1042 -0.9; 1146 -1.5; 1261 -2.2; 1387 -2.8; 1526 -3.1; 1678 -3.3; 1846 -3.5; 2031 -4.0; 2234 -4.8; 2457 -5.1; 2703 -4.9; 2973 -4.3; 3270 -3.8; 3597 -3.8; 3957 -4.6; 4353 -5.3; 4788 -5.1; 5267 -4.0; 5793 -1.9; 6373 -1.3; 7010 -3.8; 7711 -3.9; 8482 -3.0; 9330 -3.1; 10263 -3.1; 11289 -3.1; 12418 -3.1; 13660 -3.1; 15026 -3.1; 16529 -3.1; 18182 -3.1; 20000 -3.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ikko OH-1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ikko OH-1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 41 Hz   | 0.21 | -1.3 dB |
| Peaking | 190 Hz  | 0.31 | -2.0 dB |
| Peaking | 667 Hz  | 0.5  | 3.4 dB  |
| Peaking | 2293 Hz | 1.36 | -2.6 dB |
| Peaking | 4486 Hz | 5.25 | -2.3 dB |
| Peaking | 979 Hz  | 2.27 | 1.2 dB  |
| Peaking | 1338 Hz | 0.93 | -1.0 dB |
| Peaking | 1912 Hz | 3.54 | 1.1 dB  |
| Peaking | 6213 Hz | 6.38 | 2.6 dB  |
| Peaking | 7307 Hz | 7.99 | -1.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.6 dB |
| Peaking | 62 Hz    | 1.41 | -1.7 dB |
| Peaking | 125 Hz   | 1.41 | -2.2 dB |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | 1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.6 dB |
| Peaking | 4000 Hz  | 1.41 | -1.4 dB |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Ikko%20OH-1/Ikko%20OH-1.png)