# Aurisonic Rockets
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.8; 23 -6.0; 25 -6.1; 28 -6.2; 31 -6.3; 34 -6.5; 37 -6.6; 41 -6.8; 45 -6.9; 49 -7.1; 54 -7.3; 60 -7.6; 66 -7.9; 72 -8.2; 79 -8.6; 87 -9.0; 96 -9.5; 106 -9.8; 116 -9.9; 128 -10.3; 141 -10.5; 155 -10.7; 170 -10.8; 187 -10.9; 206 -10.9; 227 -10.8; 249 -10.8; 274 -10.6; 302 -10.5; 332 -10.2; 365 -10.0; 402 -9.7; 442 -9.3; 486 -9.0; 535 -8.7; 588 -8.1; 647 -7.8; 712 -7.6; 783 -7.2; 861 -7.4; 947 -7.6; 1042 -7.8; 1146 -8.0; 1261 -8.3; 1387 -8.6; 1526 -9.1; 1678 -9.5; 1846 -9.3; 2031 -8.7; 2234 -8.0; 2457 -6.5; 2703 -4.8; 2973 -2.3; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.6; 4788 -0.7; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Aurisonic Rockets GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Aurisonic Rockets ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 15 Hz   | 0.6  | 0.9 dB  |
| Peaking | 119 Hz  | 0.83 | -2.1 dB |
| Peaking | 261 Hz  | 0.67 | -3.6 dB |
| Peaking | 1899 Hz | 1.35 | -4.9 dB |
| Peaking | 3996 Hz | 0.98 | 7.6 dB  |
| Peaking | 3201 Hz | 6.52 | 1.8 dB  |
| Peaking | 4424 Hz | 2    | -1.1 dB |
| Peaking | 5514 Hz | 2.89 | 2.4 dB  |
| Peaking | 6442 Hz | 4.01 | 4.0 dB  |
| Peaking | 7106 Hz | 1.35 | -3.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.6 dB  |
| Peaking | 62 Hz    | 1.41 | -0.7 dB |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | -3.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.5 dB |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | -4.0 dB |
| Peaking | 4000 Hz  | 1.41 | 8.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Aurisonic%20Rockets/Aurisonic%20Rockets.png)