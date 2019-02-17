# Fidue A81
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.6; 23 -4.0; 25 -4.3; 28 -4.7; 31 -5.0; 34 -5.3; 37 -5.5; 41 -5.8; 45 -6.0; 49 -6.3; 54 -6.6; 60 -6.9; 66 -7.2; 72 -7.4; 79 -7.8; 87 -8.1; 96 -8.4; 106 -8.6; 116 -8.6; 128 -8.7; 141 -8.7; 155 -8.7; 170 -8.5; 187 -8.2; 206 -8.0; 227 -7.6; 249 -7.2; 274 -6.7; 302 -6.2; 332 -5.7; 365 -5.0; 402 -4.5; 442 -3.8; 486 -3.4; 535 -2.9; 588 -2.1; 647 -1.7; 712 -1.5; 783 -1.0; 861 -1.1; 947 -1.3; 1042 -1.5; 1146 -1.9; 1261 -2.3; 1387 -3.2; 1526 -4.2; 1678 -4.9; 1846 -5.5; 2031 -6.0; 2234 -7.0; 2457 -7.5; 2703 -7.3; 2973 -5.0; 3270 -2.5; 3597 -1.5; 3957 -3.2; 4353 -7.8; 4788 -12.9; 5267 -10.0; 5793 -3.6; 6373 -0.7; 7010 -0.5; 7711 -3.2; 8482 -8.4; 9330 -9.6; 10263 -6.8; 11289 -4.7; 12418 -1.6; 13660 -1.5; 15026 -1.5; 16529 -1.5; 18182 -1.5; 20000 -1.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fidue A81 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fidue A81 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 78 Hz    | 0.42 | -5.5 dB  |
| Peaking | 201 Hz   | 0.84 | -3.8 dB  |
| Peaking | 2299 Hz  | 2.09 | -6.0 dB  |
| Peaking | 4900 Hz  | 5.34 | -12.3 dB |
| Peaking | 21059 Hz | 2.11 | -5.7 dB  |
| Peaking | 835 Hz   | 2.08 | 1.4 dB   |
| Peaking | 1595 Hz  | 5.12 | -1.3 dB  |
| Peaking | 7004 Hz  | 2.55 | 5.9 dB   |
| Peaking | 9035 Hz  | 2.03 | -10.0 dB |
| Peaking | 13088 Hz | 1.55 | 1.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.9 dB |
| Peaking | 62 Hz    | 1.41 | -4.3 dB |
| Peaking | 125 Hz   | 1.41 | -6.2 dB |
| Peaking | 250 Hz   | 1.41 | -5.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.6 dB |
| Peaking | 4000 Hz  | 1.41 | -3.1 dB |
| Peaking | 8000 Hz  | 1.41 | -4.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fidue%20A81/Fidue%20A81.png)