# E-Mu Teak Rosewood Cups
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.6; 23 -4.5; 25 -5.1; 28 -5.8; 31 -6.3; 34 -6.5; 37 -6.6; 41 -6.7; 45 -6.7; 49 -6.8; 54 -6.7; 60 -6.6; 66 -6.5; 72 -6.7; 79 -7.0; 87 -7.3; 96 -7.5; 106 -7.6; 116 -7.7; 128 -7.9; 141 -8.0; 155 -8.0; 170 -7.7; 187 -7.7; 206 -7.6; 227 -7.3; 249 -7.0; 274 -6.5; 302 -6.2; 332 -6.1; 365 -5.8; 402 -5.2; 442 -4.7; 486 -4.5; 535 -4.0; 588 -3.8; 647 -4.0; 712 -4.3; 783 -3.2; 861 -3.3; 947 -4.0; 1042 -4.2; 1146 -4.1; 1261 -4.1; 1387 -4.3; 1526 -4.6; 1678 -4.3; 1846 -4.0; 2031 -3.2; 2234 -2.7; 2457 -1.5; 2703 -0.9; 2973 -0.6; 3270 -0.9; 3597 -0.5; 3957 -0.5; 4353 -1.1; 4788 -2.6; 5267 -2.7; 5793 -2.4; 6373 -2.4; 7010 -1.8; 7711 -3.9; 8482 -4.2; 9330 -6.2; 10263 -6.6; 11289 -4.2; 12418 -4.2; 13660 -5.8; 15026 -4.5; 16529 -4.2; 18182 -4.2; 20000 -4.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`E-Mu Teak Rosewood Cups GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `E-Mu Teak Rosewood Cups ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 41 Hz    | 1.11 | -2.0 dB |
| Peaking | 150 Hz   | 0.69 | -3.8 dB |
| Peaking | 3408 Hz  | 1.39 | 4.0 dB  |
| Peaking | 6793 Hz  | 5.88 | 2.0 dB  |
| Peaking | 9866 Hz  | 5.5  | -3.5 dB |
| Peaking | 767 Hz   | 1.58 | 1.0 dB  |
| Peaking | 1781 Hz  | 1.46 | -1.3 dB |
| Peaking | 2022 Hz  | 3.69 | 0.7 dB  |
| Peaking | 2573 Hz  | 5.91 | 1.2 dB  |
| Peaking | 13894 Hz | 5.91 | -1.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.6 dB |
| Peaking | 62 Hz    | 1.41 | -1.8 dB |
| Peaking | 125 Hz   | 1.41 | -3.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.0 dB |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/E-Mu%20Teak%20Rosewood%20Cups/E-Mu%20Teak%20Rosewood%20Cups.png)