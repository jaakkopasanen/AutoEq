# Sennheiser IE 80 S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.9; 23 -11.0; 25 -11.0; 28 -11.0; 31 -11.1; 34 -11.1; 37 -11.1; 41 -11.2; 45 -11.2; 49 -11.3; 54 -11.4; 60 -11.5; 66 -11.7; 72 -11.8; 79 -12.0; 87 -12.2; 96 -12.3; 106 -12.4; 116 -12.5; 128 -12.4; 141 -12.3; 155 -12.1; 170 -11.9; 187 -11.6; 206 -11.1; 227 -10.7; 249 -10.2; 274 -9.6; 302 -9.0; 332 -8.4; 365 -7.7; 402 -7.1; 442 -6.4; 486 -5.7; 535 -5.0; 588 -4.3; 647 -3.5; 712 -2.7; 783 -1.9; 861 -1.3; 947 -0.8; 1042 -0.5; 1146 -0.5; 1261 -0.5; 1387 -0.7; 1526 -1.0; 1678 -1.1; 1846 -1.0; 2031 -1.0; 2234 -1.0; 2457 -1.4; 2703 -2.0; 2973 -2.7; 3270 -3.3; 3597 -3.9; 3957 -4.6; 4353 -6.2; 4788 -8.9; 5267 -8.8; 5793 -4.4; 6373 -1.1; 7010 -2.6; 7711 -4.8; 8482 -5.1; 9330 -5.1; 10263 -5.1; 11289 -5.1; 12418 -5.1; 13660 -5.1; 15026 -5.1; 16529 -5.1; 18182 -5.1; 20000 -5.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser IE 80 S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser IE 80 S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.32 | -4.7 dB |
| Peaking | 150 Hz  | 0.46 | -6.3 dB |
| Peaking | 1043 Hz | 0.89 | 5.1 dB  |
| Peaking | 2246 Hz | 2.14 | 2.9 dB  |
| Peaking | 20 Hz   | 1.37 | -0.7 dB |
| Peaking | 3379 Hz | 2.19 | 0.8 dB  |
| Peaking | 5016 Hz | 4.02 | -5.8 dB |
| Peaking | 6432 Hz | 5.1  | 5.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.9 dB |
| Peaking | 62 Hz    | 1.41 | -4.7 dB |
| Peaking | 125 Hz   | 1.41 | -6.4 dB |
| Peaking | 250 Hz   | 1.41 | -4.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.5 dB |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Sennheiser%20IE%2080%20S/Sennheiser%20IE%2080%20S.png)