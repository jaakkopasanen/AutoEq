# Focal Elegia
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.4; 23 -6.5; 25 -6.5; 28 -6.5; 31 -6.5; 34 -6.3; 37 -6.0; 41 -5.8; 45 -5.8; 49 -5.9; 54 -6.0; 60 -6.1; 66 -6.3; 72 -6.4; 79 -6.6; 87 -6.8; 96 -6.8; 106 -6.9; 116 -6.8; 128 -6.5; 141 -6.4; 155 -6.3; 170 -6.4; 187 -6.7; 206 -7.0; 227 -7.6; 249 -8.1; 274 -8.6; 302 -9.0; 332 -9.2; 365 -9.2; 402 -9.3; 442 -9.4; 486 -9.4; 535 -9.1; 588 -8.8; 647 -8.6; 712 -8.4; 783 -8.2; 861 -8.1; 947 -8.1; 1042 -7.8; 1146 -7.5; 1261 -7.8; 1387 -8.5; 1526 -9.0; 1678 -9.6; 1846 -9.5; 2031 -6.9; 2234 -5.6; 2457 -6.1; 2703 -6.1; 2973 -5.9; 3270 -1.0; 3597 -2.1; 3957 -0.5; 4353 -0.5; 4788 -1.6; 5267 -1.8; 5793 -5.7; 6373 -5.2; 7010 -4.1; 7711 -6.2; 8482 -7.6; 9330 -6.6; 10263 -6.5; 11289 -6.5; 12418 -7.1; 13660 -6.5; 15026 -6.5; 16529 -9.1; 18182 -14.3; 20000 -13.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Elegia GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Elegia ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 451 Hz   |  0.88 | -3.0 dB |
| Peaking | 1677 Hz  |  2.91 | -3.4 dB |
| Peaking | 4002 Hz  |  2.01 | 6.4 dB  |
| Peaking | 5119 Hz  |  8.37 | 2.5 dB  |
| Peaking | 18997 Hz |  1.18 | -9.4 dB |
| Peaking | 163 Hz   |  3.67 | 0.9 dB  |
| Peaking | 2178 Hz  | 10.56 | 1.4 dB  |
| Peaking | 2843 Hz  |  8.31 | -1.3 dB |
| Peaking | 8667 Hz  | 11.01 | -1.6 dB |
| Peaking | 15246 Hz |  3.54 | 1.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.3 dB  |
| Peaking | 62 Hz    | 1.41 | 0.1 dB  |
| Peaking | 125 Hz   | 1.41 | 0.3 dB  |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | -2.7 dB |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB |
| Peaking | 2000 Hz  | 1.41 | -2.8 dB |
| Peaking | 4000 Hz  | 1.41 | 6.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | -2.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Focal%20Elegia/Focal%20Elegia.png)