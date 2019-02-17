# Sennheiser G4ME ONE
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.9; 49 -1.4; 54 -1.9; 60 -2.5; 66 -3.2; 72 -3.3; 79 -2.9; 87 -4.5; 96 -5.6; 106 -6.2; 116 -6.6; 128 -7.2; 141 -7.7; 155 -7.9; 170 -8.1; 187 -8.1; 206 -8.1; 227 -8.1; 249 -7.9; 274 -7.7; 302 -7.5; 332 -7.3; 365 -7.1; 402 -7.0; 442 -6.9; 486 -6.7; 535 -6.5; 588 -6.2; 647 -6.1; 712 -6.1; 783 -5.9; 861 -6.0; 947 -6.4; 1042 -6.5; 1146 -6.3; 1261 -5.7; 1387 -4.4; 1526 -3.2; 1678 -2.4; 1846 -2.4; 2031 -3.2; 2234 -4.4; 2457 -5.3; 2703 -5.5; 2973 -4.6; 3270 -3.1; 3597 -1.6; 3957 -0.6; 4353 -1.8; 4788 -5.8; 5267 -8.1; 5793 -6.9; 6373 -1.3; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -7.7; 16529 -13.0; 18182 -15.1; 20000 -22.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser G4ME ONE GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser G4ME ONE ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 30 Hz   |  0.31 | 6.4 dB  |
| Peaking | 152 Hz  |  0.75 | -3.5 dB |
| Peaking | 1756 Hz |  2.51 | 4.4 dB  |
| Peaking | 3875 Hz |  4.06 | 6.2 dB  |
| Peaking | 6500 Hz |  8.91 | 5.2 dB  |
| Peaking | 982 Hz  |  1.34 | 1.4 dB  |
| Peaking | 1065 Hz |  2.5  | -2.0 dB |
| Peaking | 4287 Hz | 11.5  | 2.2 dB  |
| Peaking | 5528 Hz |  4.3  | -4.2 dB |
| Peaking | 6142 Hz |  6.4  | 3.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 3.5 dB  |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -6.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sennheiser%20G4ME%20ONE/Sennheiser%20G4ME%20ONE.png)