# Astrotec AX7
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.7; 25 -0.8; 28 -1.0; 31 -1.2; 34 -1.4; 37 -1.6; 41 -1.8; 45 -2.1; 49 -2.4; 54 -2.7; 60 -3.0; 66 -3.4; 72 -3.9; 79 -4.3; 87 -4.9; 96 -5.4; 106 -5.8; 116 -6.1; 128 -6.6; 141 -7.0; 155 -7.4; 170 -7.6; 187 -7.8; 206 -8.1; 227 -8.2; 249 -8.4; 274 -8.4; 302 -8.4; 332 -8.4; 365 -8.4; 402 -8.3; 442 -8.1; 486 -8.0; 535 -7.9; 588 -7.5; 647 -7.4; 712 -7.4; 783 -7.2; 861 -7.4; 947 -7.7; 1042 -8.1; 1146 -8.3; 1261 -8.7; 1387 -9.2; 1526 -9.7; 1678 -9.8; 1846 -9.8; 2031 -9.6; 2234 -9.2; 2457 -7.8; 2703 -5.4; 2973 -1.5; 3270 -0.5; 3597 -0.5; 3957 -1.4; 4353 -6.0; 4788 -6.5; 5267 -4.6; 5793 -3.5; 6373 -2.9; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -7.2; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Astrotec AX7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Astrotec AX7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 1.06 | 5.9 dB  |
| Peaking | 54 Hz   | 1.71 | 2.9 dB  |
| Peaking | 2584 Hz | 0.48 | -5.3 dB |
| Peaking | 3349 Hz | 2.14 | 11.7 dB |
| Peaking | 6308 Hz | 2.91 | 5.1 dB  |
| Peaking | 87 Hz   | 1.41 | 1.1 dB  |
| Peaking | 298 Hz  | 0.51 | -2.1 dB |
| Peaking | 811 Hz  | 0.92 | 1.6 dB  |
| Peaking | 1941 Hz | 2.47 | -0.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 2.5 dB  |
| Peaking | 125 Hz   | 1.41 | -0.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB |
| Peaking | 2000 Hz  | 1.41 | -3.7 dB |
| Peaking | 4000 Hz  | 1.41 | 5.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Astrotec%20AX7/Astrotec%20AX7.png)