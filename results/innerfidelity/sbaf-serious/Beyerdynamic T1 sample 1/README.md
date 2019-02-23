# Beyerdynamic T1 sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.7; 31 -1.0; 34 -1.4; 37 -1.7; 41 -2.1; 45 -2.4; 49 -2.8; 54 -2.7; 60 -2.3; 66 -3.3; 72 -4.1; 79 -4.7; 87 -5.2; 96 -5.7; 106 -6.0; 116 -6.3; 128 -6.6; 141 -6.9; 155 -7.1; 170 -7.2; 187 -7.3; 206 -7.4; 227 -7.4; 249 -7.4; 274 -7.3; 302 -7.3; 332 -7.1; 365 -7.0; 402 -6.8; 442 -6.6; 486 -6.4; 535 -6.3; 588 -6.0; 647 -5.8; 712 -5.9; 783 -5.4; 861 -5.4; 947 -5.2; 1042 -5.1; 1146 -4.8; 1261 -4.6; 1387 -4.7; 1526 -5.8; 1678 -6.8; 1846 -7.0; 2031 -5.2; 2234 -3.5; 2457 -5.6; 2703 -4.9; 2973 -4.7; 3270 -3.8; 3597 -4.2; 3957 -4.3; 4353 -5.2; 4788 -1.8; 5267 -0.5; 5793 -8.4; 6373 -10.5; 7010 -7.4; 7711 -12.9; 8482 -17.5; 9330 -15.9; 10263 -8.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -7.0; 16529 -7.2; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic T1 sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T1 sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 26 Hz    |  1.01 | 6.3 dB   |
| Peaking | 58 Hz    |  2.64 | 2.8 dB   |
| Peaking | 2698 Hz  |  0.5  | 1.8 dB   |
| Peaking | 5042 Hz  |  8.35 | 6.5 dB   |
| Peaking | 8570 Hz  |  3.36 | -12.7 dB |
| Peaking | 257 Hz   |  0.83 | -1.3 dB  |
| Peaking | 1481 Hz  |  0.33 | 0.9 dB   |
| Peaking | 1762 Hz  |  4.8  | -3.2 dB  |
| Peaking | 6096 Hz  | 12.76 | -5.4 dB  |
| Peaking | 10990 Hz |  6.76 | 2.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 2.5 dB  |
| Peaking | 125 Hz   | 1.41 | -0.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.0 dB |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.2 dB |
| Peaking | 4000 Hz  | 1.41 | 5.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -7.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20T1%20sample%201/Beyerdynamic%20T1%20sample%201.png)