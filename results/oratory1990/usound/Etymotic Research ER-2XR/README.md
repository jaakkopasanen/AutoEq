# Etymotic Research ER-2XR
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.9; 23 -4.9; 25 -4.9; 28 -4.9; 31 -4.8; 34 -4.8; 37 -4.8; 41 -4.7; 45 -4.7; 49 -4.7; 54 -4.7; 60 -4.8; 66 -4.9; 72 -5.0; 79 -5.1; 87 -5.3; 96 -5.5; 106 -5.6; 116 -5.8; 128 -5.9; 141 -5.9; 155 -6.0; 170 -5.9; 187 -5.9; 206 -5.8; 227 -5.6; 249 -5.5; 274 -5.4; 302 -5.2; 332 -5.1; 365 -4.9; 402 -4.8; 442 -4.6; 486 -4.4; 535 -4.2; 588 -4.0; 647 -3.8; 712 -3.4; 783 -3.1; 861 -2.8; 947 -2.8; 1042 -3.4; 1146 -4.6; 1261 -6.3; 1387 -7.4; 1526 -7.8; 1678 -7.6; 1846 -7.3; 2031 -7.2; 2234 -7.2; 2457 -7.1; 2703 -6.8; 2973 -6.0; 3270 -5.1; 3597 -4.2; 3957 -3.3; 4353 -2.5; 4788 -2.0; 5267 -1.6; 5793 -1.1; 6373 -0.5; 7010 -1.9; 7711 -4.2; 8482 -4.4; 9330 -4.5; 10263 -5.7; 11289 -9.1; 12418 -8.4; 13660 -6.2; 15026 -6.8; 16529 -9.0; 18182 -10.8; 20000 -12.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic Research ER-2XR GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic Research ER-2XR ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.8dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 156 Hz   |  0.74 | -1.5 dB |
| Peaking | 945 Hz   |  1.25 | 5.0 dB  |
| Peaking | 1520 Hz  |  0.77 | -5.3 dB |
| Peaking | 5728 Hz  |  1.42 | 4.9 dB  |
| Peaking | 20324 Hz |  0.17 | -6.7 dB |
| Peaking | 1884 Hz  |  6.93 | 0.7 dB  |
| Peaking | 6676 Hz  | 10.6  | 2.0 dB  |
| Peaking | 9789 Hz  |  3.45 | 4.1 dB  |
| Peaking | 11412 Hz |  1.51 | -5.2 dB |
| Peaking | 14044 Hz |  1.81 | 4.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.4 dB |
| Peaking | 62 Hz    | 1.41 | -0.1 dB |
| Peaking | 125 Hz   | 1.41 | -1.4 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.9 dB |
| Peaking | 4000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -6.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Etymotic%20Research%20ER-2XR/Etymotic%20Research%20ER-2XR.png)