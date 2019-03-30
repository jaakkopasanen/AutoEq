# Astrotec AX-60
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.6; 23 -5.2; 25 -5.8; 28 -6.6; 31 -7.2; 34 -7.6; 37 -8.0; 41 -8.4; 45 -8.8; 49 -9.2; 54 -9.5; 60 -9.8; 66 -10.0; 72 -10.2; 79 -10.3; 87 -10.5; 96 -10.6; 106 -10.6; 116 -10.6; 128 -10.5; 141 -10.3; 155 -10.1; 170 -9.9; 187 -9.7; 206 -9.3; 227 -9.0; 249 -9.0; 274 -8.9; 302 -8.7; 332 -8.3; 365 -8.0; 402 -7.7; 442 -7.2; 486 -6.8; 535 -6.4; 588 -6.0; 647 -5.7; 712 -5.5; 783 -5.2; 861 -5.1; 947 -5.0; 1042 -4.8; 1146 -4.7; 1261 -4.5; 1387 -4.3; 1526 -4.0; 1678 -3.8; 1846 -4.2; 2031 -4.9; 2234 -6.1; 2457 -7.1; 2703 -7.3; 2973 -6.1; 3270 -3.7; 3597 -1.5; 3957 -1.5; 4353 -2.5; 4788 -2.2; 5267 -1.1; 5793 -0.5; 6373 -1.1; 7010 -3.5; 7711 -5.7; 8482 -6.3; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Astrotec AX-60 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Astrotec AX-60 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 66 Hz   | 0.94 | -2.2 dB |
| Peaking | 149 Hz  | 0.5  | -3.7 dB |
| Peaking | 1193 Hz | 1.13 | 1.9 dB  |
| Peaking | 3821 Hz | 4.7  | 4.2 dB  |
| Peaking | 5751 Hz | 2.91 | 5.8 dB  |
| Peaking | 18 Hz   | 2.36 | 2.2 dB  |
| Peaking | 2363 Hz | 4.38 | -2.7 dB |
| Peaking | 2504 Hz | 1.5  | 2.6 dB  |
| Peaking | 2742 Hz | 4.18 | -3.7 dB |
| Peaking | 8384 Hz | 4.29 | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.2 dB |
| Peaking | 62 Hz    | 1.41 | -3.7 dB |
| Peaking | 125 Hz   | 1.41 | -3.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.7 dB |
| Peaking | 4000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Astrotec%20AX-60/Astrotec%20AX-60.png)