# Etymotic Research ER-4XR
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.3; 23 -2.4; 25 -2.4; 28 -2.5; 31 -2.6; 34 -2.6; 37 -2.7; 41 -2.8; 45 -3.0; 49 -3.1; 54 -3.2; 60 -3.4; 66 -3.7; 72 -3.9; 79 -4.2; 87 -4.5; 96 -4.8; 106 -5.1; 116 -5.4; 128 -5.7; 141 -5.9; 155 -6.0; 170 -6.0; 187 -6.2; 206 -6.2; 227 -6.2; 249 -6.1; 274 -6.1; 302 -6.0; 332 -5.9; 365 -5.8; 402 -5.8; 442 -5.7; 486 -5.6; 535 -5.6; 588 -5.6; 647 -5.5; 712 -5.4; 783 -5.4; 861 -5.5; 947 -6.0; 1042 -6.6; 1146 -7.4; 1261 -8.1; 1387 -8.6; 1526 -8.7; 1678 -8.6; 1846 -8.4; 2031 -8.3; 2234 -8.4; 2457 -8.5; 2703 -8.2; 2973 -7.6; 3270 -6.9; 3597 -6.3; 3957 -5.7; 4353 -5.2; 4788 -4.5; 5267 -3.3; 5793 -1.6; 6373 -0.5; 7010 -3.3; 7711 -5.5; 8482 -5.8; 9330 -6.3; 10263 -8.7; 11289 -10.1; 12418 -11.5; 13660 -12.2; 15026 -10.2; 16529 -5.9; 18182 -5.8; 20000 -5.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic Research ER-4XR GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic Research ER-4XR ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 0.82 | 3.4 dB  |
| Peaking | 59 Hz    | 1.45 | 1.6 dB  |
| Peaking | 1942 Hz  | 1.08 | -3.1 dB |
| Peaking | 6151 Hz  | 2.69 | 6.0 dB  |
| Peaking | 13124 Hz | 1.52 | -6.9 dB |
| Peaking | 200 Hz   | 1.65 | -0.6 dB |
| Peaking | 875 Hz   | 1.22 | 2.0 dB  |
| Peaking | 1296 Hz  | 1.05 | -2.0 dB |
| Peaking | 1883 Hz  | 3.14 | 1.4 dB  |
| Peaking | 16843 Hz | 4.02 | 1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.6 dB  |
| Peaking | 62 Hz    | 1.41 | 1.8 dB  |
| Peaking | 125 Hz   | 1.41 | -0.2 dB |
| Peaking | 250 Hz   | 1.41 | -0.6 dB |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | -3.9 dB |
| Peaking | 4000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -4.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Etymotic%20Research%20ER-4XR/Etymotic%20Research%20ER-4XR.png)