# Bose QuietComfort 15
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.0; 23 -8.4; 25 -8.8; 28 -9.2; 31 -9.5; 34 -9.6; 37 -9.7; 41 -9.8; 45 -9.9; 49 -9.8; 54 -9.8; 60 -9.8; 66 -9.8; 72 -9.8; 79 -10.1; 87 -10.4; 96 -10.7; 106 -10.7; 116 -10.6; 128 -10.7; 141 -10.6; 155 -10.4; 170 -9.9; 187 -9.9; 206 -9.7; 227 -9.5; 249 -9.3; 274 -9.0; 302 -8.6; 332 -8.2; 365 -7.7; 402 -7.3; 442 -6.9; 486 -6.7; 535 -6.4; 588 -5.9; 647 -5.6; 712 -5.5; 783 -5.3; 861 -5.7; 947 -6.2; 1042 -6.6; 1146 -7.3; 1261 -7.8; 1387 -7.9; 1526 -8.3; 1678 -9.1; 1846 -9.5; 2031 -9.1; 2234 -8.5; 2457 -8.2; 2703 -6.8; 2973 -5.3; 3270 -3.4; 3597 -0.5; 3957 -7.6; 4353 -11.8; 4788 -9.1; 5267 -4.9; 5793 -9.5; 6373 -10.2; 7010 -6.5; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose QuietComfort 15 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 15 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 47 Hz   | 0.43 | -2.9 dB |
| Peaking | 153 Hz  | 0.84 | -3.0 dB |
| Peaking | 1918 Hz | 2.08 | -3.2 dB |
| Peaking | 3637 Hz | 4.25 | 10.5 dB |
| Peaking | 4193 Hz | 3.91 | -9.1 dB |
| Peaking | 283 Hz  | 3.07 | -0.7 dB |
| Peaking | 712 Hz  | 2.21 | 1.7 dB  |
| Peaking | 5350 Hz | 7.24 | 5.5 dB  |
| Peaking | 6076 Hz | 3.65 | -5.6 dB |
| Peaking | 7204 Hz | 4.85 | 2.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.7 dB |
| Peaking | 62 Hz    | 1.41 | -2.5 dB |
| Peaking | 125 Hz   | 1.41 | -3.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.6 dB |
| Peaking | 4000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bose%20QuietComfort%2015/Bose%20QuietComfort%2015.png)