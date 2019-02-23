# Bose QuietControl 30
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.6; 23 -5.7; 25 -5.8; 28 -5.8; 31 -5.7; 34 -5.5; 37 -5.3; 41 -5.0; 45 -4.7; 49 -4.5; 54 -4.3; 60 -4.2; 66 -4.3; 72 -4.4; 79 -4.5; 87 -4.7; 96 -4.9; 106 -5.0; 116 -5.1; 128 -5.1; 141 -5.1; 155 -5.0; 170 -4.8; 187 -4.5; 206 -4.2; 227 -4.0; 249 -3.8; 274 -3.6; 302 -3.5; 332 -3.5; 365 -3.5; 402 -3.3; 442 -2.8; 486 -2.1; 535 -1.5; 588 -1.0; 647 -0.7; 712 -0.6; 783 -0.5; 861 -1.0; 947 -1.7; 1042 -2.3; 1146 -2.5; 1261 -2.6; 1387 -2.6; 1526 -3.0; 1678 -3.9; 1846 -5.0; 2031 -5.3; 2234 -4.2; 2457 -2.8; 2703 -2.4; 2973 -2.7; 3270 -3.0; 3597 -3.4; 3957 -4.4; 4353 -6.9; 4788 -6.1; 5267 -5.2; 5793 -3.6; 6373 -3.0; 7010 -1.2; 7711 -2.5; 8482 -2.8; 9330 -2.8; 10263 -3.9; 11289 -2.8; 12418 -2.8; 13660 -2.8; 15026 -5.6; 16529 -4.9; 18182 -2.8; 20000 -2.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose QuietControl 30 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietControl 30 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 26 Hz    | 0.98 | -3.0 dB |
| Peaking | 133 Hz   | 0.69 | -2.2 dB |
| Peaking | 707 Hz   | 1.75 | 2.7 dB  |
| Peaking | 1946 Hz  | 4.78 | -2.8 dB |
| Peaking | 4556 Hz  | 4.42 | -4.4 dB |
| Peaking | 2792 Hz  | 4.84 | 0.9 dB  |
| Peaking | 5663 Hz  | 1.87 | -0.4 dB |
| Peaking | 7098 Hz  | 6.67 | 2.0 dB  |
| Peaking | 15810 Hz | 3.87 | -4.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.1 dB |
| Peaking | 62 Hz    | 1.41 | -0.5 dB |
| Peaking | 125 Hz   | 1.41 | -2.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB |
| Peaking | 4000 Hz  | 1.41 | -1.9 dB |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -2.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bose%20QuietControl%2030/Bose%20QuietControl%2030.png)