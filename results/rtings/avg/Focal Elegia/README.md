# Focal Elegia
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.2; 23 -6.3; 25 -6.3; 28 -6.3; 31 -6.2; 34 -6.0; 37 -5.9; 41 -5.7; 45 -5.7; 49 -5.7; 54 -5.8; 60 -5.9; 66 -6.1; 72 -6.2; 79 -6.4; 87 -6.6; 96 -6.7; 106 -6.7; 116 -6.6; 128 -6.3; 141 -6.2; 155 -6.1; 170 -6.2; 187 -6.4; 206 -6.9; 227 -7.5; 249 -8.1; 274 -8.6; 302 -9.0; 332 -9.2; 365 -9.2; 402 -9.2; 442 -9.4; 486 -9.5; 535 -9.2; 588 -8.9; 647 -8.7; 712 -8.5; 783 -8.3; 861 -8.1; 947 -8.2; 1042 -7.8; 1146 -7.6; 1261 -7.9; 1387 -8.6; 1526 -9.2; 1678 -9.9; 1846 -9.8; 2031 -7.4; 2234 -6.4; 2457 -7.1; 2703 -6.6; 2973 -6.0; 3270 -0.9; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.9; 5267 -2.3; 5793 -5.5; 6373 -4.4; 7010 -4.1; 7711 -6.2; 8482 -7.2; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -7.3; 13660 -6.5; 15026 -6.5; 16529 -8.9; 18182 -14.1; 20000 -13.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Elegia GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Elegia ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 105 Hz   | 0.21 | 0.6 dB  |
| Peaking | 427 Hz   | 0.8  | -3.4 dB |
| Peaking | 1726 Hz  | 1.94 | -3.5 dB |
| Peaking | 4059 Hz  | 1.76 | 7.0 dB  |
| Peaking | 18996 Hz | 1.18 | -9.2 dB |
| Peaking | 2134 Hz  | 8.77 | 1.9 dB  |
| Peaking | 2966 Hz  | 3.02 | -2.8 dB |
| Peaking | 3318 Hz  | 7.02 | 4.1 dB  |
| Peaking | 15259 Hz | 3.84 | 1.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.5 dB  |
| Peaking | 62 Hz    | 1.41 | 0.3 dB  |
| Peaking | 125 Hz   | 1.41 | 0.5 dB  |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | -2.8 dB |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | -3.5 dB |
| Peaking | 4000 Hz  | 1.41 | 7.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | -2.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Focal%20Elegia/Focal%20Elegia.png)