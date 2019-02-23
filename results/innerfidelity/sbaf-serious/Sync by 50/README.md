# Sync by 50
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.2; 23 -6.0; 25 -6.7; 28 -7.7; 31 -8.5; 34 -9.1; 37 -9.7; 41 -10.3; 45 -10.8; 49 -11.2; 54 -11.6; 60 -11.9; 66 -12.2; 72 -12.4; 79 -12.7; 87 -13.0; 96 -13.4; 106 -13.4; 116 -13.5; 128 -13.7; 141 -13.7; 155 -13.7; 170 -13.4; 187 -13.2; 206 -12.9; 227 -12.3; 249 -12.1; 274 -12.5; 302 -12.5; 332 -12.2; 365 -11.9; 402 -11.7; 442 -11.5; 486 -11.2; 535 -9.8; 588 -6.8; 647 -3.8; 712 -2.0; 783 -1.3; 861 -2.1; 947 -3.1; 1042 -4.0; 1146 -4.4; 1261 -4.0; 1387 -3.3; 1526 -4.5; 1678 -6.0; 1846 -6.7; 2031 -6.7; 2234 -5.9; 2457 -4.7; 2703 -3.3; 2973 -2.3; 3270 -2.1; 3597 -2.9; 3957 -3.9; 4353 -3.4; 4788 -0.8; 5267 -0.5; 5793 -1.1; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sync by 50 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sync by 50 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 54 Hz   | 1.32 | -2.0 dB |
| Peaking | 133 Hz  | 0.51 | -6.7 dB |
| Peaking | 518 Hz  | 1    | -9.6 dB |
| Peaking | 705 Hz  | 1.16 | 12.0 dB |
| Peaking | 5067 Hz | 1.35 | 5.7 dB  |
| Peaking | 2043 Hz | 2.63 | -3.5 dB |
| Peaking | 3213 Hz | 0.86 | 3.4 dB  |
| Peaking | 4140 Hz | 4.46 | -4.4 dB |
| Peaking | 6440 Hz | 4.51 | 3.5 dB  |
| Peaking | 7281 Hz | 1.43 | -3.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.8 dB |
| Peaking | 62 Hz    | 1.41 | -4.8 dB |
| Peaking | 125 Hz   | 1.41 | -5.9 dB |
| Peaking | 250 Hz   | 1.41 | -5.3 dB |
| Peaking | 500 Hz   | 1.41 | -2.9 dB |
| Peaking | 1000 Hz  | 1.41 | 5.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.5 dB |
| Peaking | 4000 Hz  | 1.41 | 5.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sync%20by%2050/Sync%20by%2050.png)