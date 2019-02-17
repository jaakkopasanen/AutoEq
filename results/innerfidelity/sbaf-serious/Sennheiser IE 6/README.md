# Sennheiser IE 6
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.3; 23 -9.7; 25 -10.0; 28 -10.3; 31 -10.6; 34 -11.0; 37 -11.2; 41 -11.6; 45 -11.9; 49 -12.1; 54 -12.4; 60 -12.8; 66 -13.0; 72 -13.4; 79 -13.7; 87 -14.1; 96 -14.3; 106 -14.5; 116 -14.5; 128 -14.6; 141 -14.6; 155 -14.6; 170 -14.4; 187 -14.2; 206 -13.9; 227 -13.5; 249 -13.1; 274 -12.6; 302 -12.1; 332 -11.5; 365 -10.8; 402 -10.2; 442 -9.5; 486 -9.0; 535 -8.3; 588 -7.4; 647 -6.8; 712 -6.4; 783 -5.8; 861 -5.7; 947 -5.8; 1042 -5.9; 1146 -5.9; 1261 -6.1; 1387 -6.5; 1526 -6.6; 1678 -7.0; 1846 -7.1; 2031 -7.0; 2234 -7.1; 2457 -7.0; 2703 -7.2; 2973 -6.5; 3270 -5.9; 3597 -6.0; 3957 -8.3; 4353 -13.3; 4788 -15.2; 5267 -8.6; 5793 -3.1; 6373 -0.5; 7010 -3.4; 7711 -5.6; 8482 -5.9; 9330 -5.9; 10263 -5.9; 11289 -5.9; 12418 -5.9; 13660 -5.9; 15026 -5.9; 16529 -5.9; 18182 -5.9; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser IE 6 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser IE 6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 58 Hz   | 0.37 | -5.5 dB  |
| Peaking | 150 Hz  | 0.74 | -4.8 dB  |
| Peaking | 300 Hz  | 1.2  | -2.9 dB  |
| Peaking | 4676 Hz | 4.78 | -11.3 dB |
| Peaking | 6233 Hz | 4.36 | 7.1 dB   |
| Peaking | 489 Hz  | 2.47 | -0.8 dB  |
| Peaking | 862 Hz  | 1.12 | 1.3 dB   |
| Peaking | 2095 Hz | 0.92 | -1.3 dB  |
| Peaking | 3512 Hz | 5.18 | 2.1 dB   |
| Peaking | 8159 Hz | 5.63 | -0.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.0 dB |
| Peaking | 62 Hz    | 1.41 | -5.4 dB |
| Peaking | 125 Hz   | 1.41 | -7.4 dB |
| Peaking | 250 Hz   | 1.41 | -6.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.5 dB |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.3 dB |
| Peaking | 4000 Hz  | 1.41 | -3.9 dB |
| Peaking | 8000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20IE%206/Sennheiser%20IE%206.png)