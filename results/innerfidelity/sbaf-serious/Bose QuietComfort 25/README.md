# Bose QuietComfort 25
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.4; 23 -7.8; 25 -8.0; 28 -7.9; 31 -7.6; 34 -7.3; 37 -6.9; 41 -6.8; 45 -7.0; 49 -7.2; 54 -7.5; 60 -7.8; 66 -7.9; 72 -7.9; 79 -8.0; 87 -7.9; 96 -7.9; 106 -7.8; 116 -7.6; 128 -7.6; 141 -7.6; 155 -7.6; 170 -7.2; 187 -7.1; 206 -7.2; 227 -7.0; 249 -6.8; 274 -6.7; 302 -6.5; 332 -6.2; 365 -5.8; 402 -5.5; 442 -5.1; 486 -5.0; 535 -4.7; 588 -4.4; 647 -4.4; 712 -4.5; 783 -4.7; 861 -5.4; 947 -6.0; 1042 -6.1; 1146 -5.9; 1261 -6.1; 1387 -6.8; 1526 -8.4; 1678 -10.2; 1846 -11.9; 2031 -12.3; 2234 -11.2; 2457 -10.5; 2703 -10.1; 2973 -11.0; 3270 -12.5; 3597 -11.6; 3957 -8.6; 4353 -5.4; 4788 -2.2; 5267 -0.5; 5793 -2.7; 6373 -5.6; 7010 -4.1; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose QuietComfort 25 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 25 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 113 Hz  | 0.21 | -1.4 dB |
| Peaking | 600 Hz  | 0.73 | 2.7 dB  |
| Peaking | 1967 Hz | 2.48 | -6.0 dB |
| Peaking | 3394 Hz | 2.67 | -6.4 dB |
| Peaking | 5145 Hz | 3.07 | 7.3 dB  |
| Peaking | 45 Hz   | 3.73 | 0.6 dB  |
| Peaking | 975 Hz  | 6.55 | -0.8 dB |
| Peaking | 1239 Hz | 4.32 | 0.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.8 dB |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | -0.6 dB |
| Peaking | 500 Hz   | 1.41 | 1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.4 dB |
| Peaking | 4000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bose%20QuietComfort%2025/Bose%20QuietComfort%2025.png)