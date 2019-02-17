# Xiaomi Hybrid
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.9; 23 -12.2; 25 -12.5; 28 -12.9; 31 -13.1; 34 -13.3; 37 -13.4; 41 -13.6; 45 -13.8; 49 -13.9; 54 -14.0; 60 -14.1; 66 -14.2; 72 -14.3; 79 -14.4; 87 -14.5; 96 -14.7; 106 -14.5; 116 -14.3; 128 -14.2; 141 -14.0; 155 -13.8; 170 -13.4; 187 -13.0; 206 -12.7; 227 -12.2; 249 -11.7; 274 -11.0; 302 -10.4; 332 -9.9; 365 -9.3; 402 -8.7; 442 -8.0; 486 -7.6; 535 -7.1; 588 -6.4; 647 -6.1; 712 -5.9; 783 -5.7; 861 -5.8; 947 -6.2; 1042 -6.6; 1146 -7.2; 1261 -7.6; 1387 -8.8; 1526 -10.0; 1678 -11.2; 1846 -12.0; 2031 -12.5; 2234 -12.5; 2457 -10.6; 2703 -8.3; 2973 -6.2; 3270 -5.0; 3597 -6.1; 3957 -7.8; 4353 -6.6; 4788 -3.2; 5267 -0.6; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.7; 15026 -8.5; 16529 -6.6; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Xiaomi Hybrid GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Xiaomi Hybrid ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 39 Hz    | 0.4  | -6.5 dB |
| Peaking | 120 Hz   | 0.85 | -4.5 dB |
| Peaking | 235 Hz   | 1.42 | -2.9 dB |
| Peaking | 2009 Hz  | 2.34 | -6.8 dB |
| Peaking | 5733 Hz  | 3.02 | 7.1 dB  |
| Peaking | 788 Hz   | 1.12 | 3.8 dB  |
| Peaking | 847 Hz   | 0.58 | -2.3 dB |
| Peaking | 3226 Hz  | 4.68 | 2.6 dB  |
| Peaking | 4054 Hz  | 8.08 | -2.6 dB |
| Peaking | 14903 Hz | 4.02 | -2.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.3 dB |
| Peaking | 62 Hz    | 1.41 | -6.0 dB |
| Peaking | 125 Hz   | 1.41 | -6.6 dB |
| Peaking | 250 Hz   | 1.41 | -4.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.0 dB |
| Peaking | 4000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 16000 Hz | 1.41 | -1.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Xiaomi%20Hybrid/Xiaomi%20Hybrid.png)