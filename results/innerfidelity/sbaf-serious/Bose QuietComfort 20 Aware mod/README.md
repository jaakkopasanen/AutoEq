# Bose QuietComfort 20 Aware mod
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.6; 23 -3.1; 25 -4.2; 28 -5.4; 31 -5.9; 34 -6.1; 37 -6.0; 41 -5.8; 45 -5.6; 49 -5.4; 54 -5.3; 60 -5.3; 66 -5.6; 72 -6.0; 79 -6.5; 87 -7.0; 96 -7.6; 106 -7.9; 116 -7.9; 128 -8.0; 141 -7.9; 155 -7.9; 170 -7.9; 187 -7.9; 206 -7.9; 227 -7.8; 249 -7.7; 274 -7.5; 302 -7.3; 332 -7.2; 365 -7.1; 402 -7.2; 442 -7.1; 486 -7.2; 535 -6.9; 588 -6.3; 647 -6.2; 712 -6.4; 783 -5.6; 861 -5.2; 947 -5.2; 1042 -5.8; 1146 -6.7; 1261 -7.8; 1387 -9.4; 1526 -11.0; 1678 -11.7; 1846 -10.6; 2031 -9.0; 2234 -8.1; 2457 -7.0; 2703 -6.4; 2973 -4.6; 3270 -3.1; 3597 -3.5; 3957 -5.7; 4353 -7.5; 4788 -4.0; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.5; 7711 -9.2; 8482 -7.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose QuietComfort 20 Aware mod GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 20 Aware mod ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 2.27 | 5.7 dB  |
| Peaking | 1683 Hz | 3    | -5.6 dB |
| Peaking | 3304 Hz | 5.96 | 3.7 dB  |
| Peaking | 5917 Hz | 2.87 | 7.2 dB  |
| Peaking | 7758 Hz | 5.71 | -4.7 dB |
| Peaking | 59 Hz   | 1.2  | 3.2 dB  |
| Peaking | 87 Hz   | 0.39 | -2.1 dB |
| Peaking | 430 Hz  | 0.08 | -0.2 dB |
| Peaking | 928 Hz  | 2.01 | 2.1 dB  |
| Peaking | 1379 Hz | 5.08 | -0.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.4 dB  |
| Peaking | 62 Hz    | 1.41 | 0.9 dB  |
| Peaking | 125 Hz   | 1.41 | -1.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.6 dB |
| Peaking | 4000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bose%20QuietComfort%2020%20Aware%20mod/Bose%20QuietComfort%2020%20Aware%20mod.png)