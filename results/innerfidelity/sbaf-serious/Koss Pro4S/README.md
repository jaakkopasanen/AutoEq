# Koss Pro4S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.6; 23 -5.2; 25 -5.8; 28 -6.4; 31 -6.9; 34 -7.3; 37 -7.7; 41 -8.0; 45 -8.3; 49 -8.6; 54 -8.8; 60 -9.0; 66 -9.3; 72 -9.5; 79 -9.6; 87 -9.8; 96 -9.9; 106 -9.6; 116 -9.2; 128 -8.1; 141 -7.3; 155 -7.9; 170 -6.6; 187 -5.0; 206 -4.8; 227 -4.0; 249 -2.5; 274 -3.6; 302 -5.6; 332 -7.1; 365 -7.3; 402 -7.5; 442 -7.6; 486 -8.0; 535 -8.2; 588 -8.0; 647 -8.2; 712 -8.3; 783 -8.3; 861 -8.3; 947 -8.1; 1042 -7.9; 1146 -8.2; 1261 -8.6; 1387 -9.0; 1526 -9.3; 1678 -9.5; 1846 -9.8; 2031 -10.1; 2234 -10.0; 2457 -11.0; 2703 -11.3; 2973 -10.6; 3270 -9.3; 3597 -8.1; 3957 -5.5; 4353 -2.9; 4788 -0.5; 5267 -0.5; 5793 -1.1; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss Pro4S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss Pro4S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 56 Hz   | 1.58 | -1.8 dB |
| Peaking | 95 Hz   | 1.55 | -3.1 dB |
| Peaking | 244 Hz  | 3.58 | 4.4 dB  |
| Peaking | 3588 Hz | 0.51 | -8.6 dB |
| Peaking | 5097 Hz | 1.26 | 14.1 dB |
| Peaking | 21 Hz   | 2.33 | 2.2 dB  |
| Peaking | 185 Hz  | 9.7  | 1.4 dB  |
| Peaking | 503 Hz  | 1.77 | -1.2 dB |
| Peaking | 6524 Hz | 6.6  | 2.9 dB  |
| Peaking | 7332 Hz | 2.7  | -1.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.5 dB  |
| Peaking | 62 Hz    | 1.41 | -3.1 dB |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | 3.9 dB  |
| Peaking | 500 Hz   | 1.41 | -2.4 dB |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | -5.4 dB |
| Peaking | 4000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Koss%20Pro4S/Koss%20Pro4S.png)