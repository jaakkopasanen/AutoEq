# Klipsch Image One B
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.6; 23 -12.8; 25 -13.0; 28 -13.2; 31 -13.3; 34 -13.3; 37 -13.4; 41 -13.4; 45 -13.5; 49 -13.5; 54 -13.4; 60 -13.5; 66 -13.5; 72 -13.6; 79 -13.6; 87 -13.7; 96 -13.8; 106 -13.5; 116 -13.1; 128 -13.2; 141 -13.4; 155 -13.4; 170 -12.8; 187 -12.9; 206 -12.4; 227 -12.0; 249 -11.6; 274 -11.2; 302 -10.5; 332 -9.5; 365 -8.1; 402 -6.7; 442 -5.0; 486 -4.1; 535 -3.2; 588 -2.4; 647 -1.8; 712 -1.2; 783 -1.1; 861 -2.1; 947 -3.1; 1042 -3.0; 1146 -4.3; 1261 -5.2; 1387 -6.0; 1526 -6.8; 1678 -7.6; 1846 -8.3; 2031 -8.9; 2234 -9.4; 2457 -9.9; 2703 -10.7; 2973 -10.5; 3270 -9.3; 3597 -7.2; 3957 -4.9; 4353 -3.6; 4788 -1.8; 5267 -3.2; 5793 -3.5; 6373 -1.7; 7010 -0.5; 7711 -2.7; 8482 -3.0; 9330 -3.0; 10263 -3.4; 11289 -3.2; 12418 -3.0; 13660 -3.0; 15026 -3.0; 16529 -3.0; 18182 -3.0; 20000 -3.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Klipsch Image One B GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch Image One B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.8dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 31 Hz   |  0.22 | -9.6 dB  |
| Peaking | 273 Hz  |  0.42 | -8.1 dB  |
| Peaking | 640 Hz  |  0.78 | 8.0 dB   |
| Peaking | 3004 Hz |  0.73 | -13.6 dB |
| Peaking | 4361 Hz |  0.8  | 9.0 dB   |
| Peaking | 441 Hz  | 10.52 | 0.6 dB   |
| Peaking | 4992 Hz |  4.49 | 2.4 dB   |
| Peaking | 5456 Hz |  4.71 | -2.8 dB  |
| Peaking | 6787 Hz |  7.23 | 3.8 dB   |
| Peaking | 6794 Hz |  1.29 | -0.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.2 dB |
| Peaking | 62 Hz    | 1.41 | -7.7 dB  |
| Peaking | 125 Hz   | 1.41 | -8.0 dB  |
| Peaking | 250 Hz   | 1.41 | -8.2 dB  |
| Peaking | 500 Hz   | 1.41 | 1.3 dB   |
| Peaking | 1000 Hz  | 1.41 | 2.3 dB   |
| Peaking | 2000 Hz  | 1.41 | -7.7 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.6 dB   |
| Peaking | 16000 Hz | 1.41 | -0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Klipsch%20Image%20One%20B/Klipsch%20Image%20One%20B.png)