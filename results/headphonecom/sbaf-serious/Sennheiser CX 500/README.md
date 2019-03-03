# Sennheiser CX 500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.2; 23 -11.2; 25 -11.3; 28 -11.3; 31 -11.3; 34 -11.3; 37 -11.4; 41 -11.5; 45 -11.6; 49 -11.8; 54 -12.0; 60 -12.2; 66 -12.3; 72 -12.6; 79 -12.9; 87 -13.0; 96 -13.3; 106 -13.4; 116 -13.4; 128 -13.5; 141 -13.6; 155 -13.6; 170 -13.5; 187 -13.3; 206 -13.0; 227 -12.7; 249 -12.3; 274 -11.9; 302 -11.3; 332 -10.7; 365 -9.9; 402 -9.3; 442 -8.8; 486 -8.2; 535 -7.5; 588 -6.7; 647 -6.0; 712 -5.3; 783 -4.8; 861 -4.4; 947 -4.1; 1042 -4.0; 1146 -4.0; 1261 -3.9; 1387 -4.0; 1526 -4.3; 1678 -4.4; 1846 -4.2; 2031 -3.7; 2234 -3.0; 2457 -1.9; 2703 -0.7; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.6; 4788 -3.8; 5267 -5.7; 5793 -10.8; 6373 -8.8; 7010 -4.4; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser CX 500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser CX 500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.28 | -4.6 dB |
| Peaking | 140 Hz  | 0.81 | -4.5 dB |
| Peaking | 271 Hz  | 1.46 | -3.0 dB |
| Peaking | 3261 Hz | 0.67 | 6.0 dB  |
| Peaking | 5967 Hz | 5.32 | -8.7 dB |
| Peaking | 944 Hz  | 1.79 | 1.9 dB  |
| Peaking | 1906 Hz | 2.84 | -1.6 dB |
| Peaking | 3941 Hz | 3.59 | 1.2 dB  |
| Peaking | 6887 Hz | 6.47 | 3.0 dB  |
| Peaking | 7806 Hz | 1.03 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.5 dB |
| Peaking | 62 Hz    | 1.41 | -4.2 dB |
| Peaking | 125 Hz   | 1.41 | -6.0 dB |
| Peaking | 250 Hz   | 1.41 | -5.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20CX%20500/Sennheiser%20CX%20500.png)