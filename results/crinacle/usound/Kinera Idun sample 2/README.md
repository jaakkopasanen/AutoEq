# Kinera Idun sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.2; 23 -1.4; 25 -1.5; 28 -1.7; 31 -1.9; 34 -2.0; 37 -2.2; 41 -2.4; 45 -2.6; 49 -2.8; 54 -3.0; 60 -3.2; 66 -3.5; 72 -3.8; 79 -4.1; 87 -4.5; 96 -4.9; 106 -5.3; 116 -5.6; 128 -6.0; 141 -6.3; 155 -6.4; 170 -6.5; 187 -6.6; 206 -6.6; 227 -6.6; 249 -6.4; 274 -6.2; 302 -6.0; 332 -5.7; 365 -5.4; 402 -5.0; 442 -4.7; 486 -4.4; 535 -4.3; 588 -4.1; 647 -4.0; 712 -4.0; 783 -4.1; 861 -4.5; 947 -5.4; 1042 -6.6; 1146 -7.3; 1261 -7.5; 1387 -7.1; 1526 -6.1; 1678 -4.7; 1846 -3.3; 2031 -2.3; 2234 -1.8; 2457 -1.9; 2703 -2.7; 2973 -3.8; 3270 -3.7; 3597 -2.3; 3957 -1.3; 4353 -0.8; 4788 -0.5; 5267 -2.4; 5793 -4.6; 6373 -4.1; 7010 -5.2; 7711 -8.0; 8482 -6.5; 9330 -4.7; 10263 -4.7; 11289 -4.7; 12418 -5.8; 13660 -6.4; 15026 -6.3; 16529 -4.7; 18182 -4.7; 20000 -8.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Kinera Idun sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Kinera Idun sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 27 Hz    | 1.06 | 3.5 dB  |
| Peaking | 1275 Hz  | 2.77 | -3.5 dB |
| Peaking | 2215 Hz  | 2.55 | 3.2 dB  |
| Peaking | 4480 Hz  | 2.84 | 4.4 dB  |
| Peaking | 7861 Hz  | 5.7  | -4.1 dB |
| Peaking | 63 Hz    | 1.31 | 1.2 dB  |
| Peaking | 195 Hz   | 0.66 | -2.2 dB |
| Peaking | 637 Hz   | 1.1  | 1.4 dB  |
| Peaking | 1055 Hz  | 5.84 | -1.1 dB |
| Peaking | 14100 Hz | 2.8  | -2.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.2 dB  |
| Peaking | 62 Hz    | 1.41 | 1.2 dB  |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | 1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.3 dB |
| Peaking | 2000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.0 dB |
| Peaking | 16000 Hz | 1.41 | -1.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Kinera%20Idun%20sample%202/Kinera%20Idun%20sample%202.png)