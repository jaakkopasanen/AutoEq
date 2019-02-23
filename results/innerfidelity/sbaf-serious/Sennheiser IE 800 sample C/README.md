# Sennheiser IE 800 sample C
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.0; 23 -10.1; 25 -10.2; 28 -10.3; 31 -10.4; 34 -10.4; 37 -10.5; 41 -10.6; 45 -10.7; 49 -10.8; 54 -10.9; 60 -11.1; 66 -11.2; 72 -11.4; 79 -11.6; 87 -11.7; 96 -11.9; 106 -11.9; 116 -11.8; 128 -11.8; 141 -11.8; 155 -11.6; 170 -11.4; 187 -11.1; 206 -10.9; 227 -10.5; 249 -10.2; 274 -9.8; 302 -9.4; 332 -9.0; 365 -8.7; 402 -8.3; 442 -7.9; 486 -7.6; 535 -7.3; 588 -6.8; 647 -6.7; 712 -6.7; 783 -6.4; 861 -6.7; 947 -7.0; 1042 -7.3; 1146 -7.6; 1261 -7.8; 1387 -7.5; 1526 -8.0; 1678 -7.7; 1846 -6.8; 2031 -5.4; 2234 -3.8; 2457 -1.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.7; 5267 -3.3; 5793 -5.7; 6373 -2.0; 7010 -4.0; 7711 -6.2; 8482 -8.1; 9330 -12.1; 10263 -14.5; 11289 -11.5; 12418 -6.7; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser IE 800 sample C GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser IE 800 sample C ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 0.46 | -2.7 dB |
| Peaking | 127 Hz   | 0.44 | -5.0 dB |
| Peaking | 3701 Hz  | 1.2  | 7.0 dB  |
| Peaking | 10189 Hz | 3.54 | -9.4 dB |
| Peaking | 689 Hz   | 1.14 | 1.7 dB  |
| Peaking | 1488 Hz  | 0.4  | -1.5 dB |
| Peaking | 1627 Hz  | 1.86 | -1.4 dB |
| Peaking | 2580 Hz  | 3.18 | 3.7 dB  |
| Peaking | 6601 Hz  | 9.63 | 4.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.6 dB |
| Peaking | 62 Hz    | 1.41 | -3.5 dB |
| Peaking | 125 Hz   | 1.41 | -4.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB |
| Peaking | 2000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.5 dB |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20IE%20800%20sample%20C/Sennheiser%20IE%20800%20sample%20C.png)