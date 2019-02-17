# Bose QuietComfort 25
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.6; 23 -8.0; 25 -8.2; 28 -8.1; 31 -7.8; 34 -7.4; 37 -7.1; 41 -7.0; 45 -7.2; 49 -7.4; 54 -7.7; 60 -7.9; 66 -8.0; 72 -8.1; 79 -8.2; 87 -8.1; 96 -8.0; 106 -7.9; 116 -7.8; 128 -7.8; 141 -7.8; 155 -7.7; 170 -7.4; 187 -7.3; 206 -7.4; 227 -7.2; 249 -7.0; 274 -6.9; 302 -6.6; 332 -6.3; 365 -6.0; 402 -5.7; 442 -5.2; 486 -5.1; 535 -4.9; 588 -4.5; 647 -4.5; 712 -4.7; 783 -4.9; 861 -5.5; 947 -6.2; 1042 -6.2; 1146 -6.0; 1261 -6.2; 1387 -7.0; 1526 -8.6; 1678 -10.4; 1846 -12.0; 2031 -12.5; 2234 -11.4; 2457 -10.6; 2703 -10.2; 2973 -11.2; 3270 -12.6; 3597 -11.8; 3957 -8.8; 4353 -5.5; 4788 -2.4; 5267 -0.5; 5793 -2.9; 6373 -5.7; 7010 -4.1; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
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
| Peaking | 103 Hz  | 0.2  | -1.5 dB |
| Peaking | 596 Hz  | 0.77 | 2.6 dB  |
| Peaking | 1968 Hz | 2.46 | -6.1 dB |
| Peaking | 3391 Hz | 2.67 | -6.5 dB |
| Peaking | 5149 Hz | 3.2  | 7.3 dB  |
| Peaking | 42 Hz   | 3.74 | 0.7 dB  |
| Peaking | 969 Hz  | 6.51 | -0.8 dB |
| Peaking | 1228 Hz | 4.3  | 0.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.9 dB |
| Peaking | 62 Hz    | 1.41 | -1.1 dB |
| Peaking | 125 Hz   | 1.41 | -1.2 dB |
| Peaking | 250 Hz   | 1.41 | -0.7 dB |
| Peaking | 500 Hz   | 1.41 | 1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.5 dB |
| Peaking | 4000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bose%20QuietComfort%2025/Bose%20QuietComfort%2025.png)