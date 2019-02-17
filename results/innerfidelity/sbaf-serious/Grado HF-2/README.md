# Grado HF-2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.8; 45 -1.8; 49 -3.0; 54 -4.0; 60 -5.4; 66 -6.6; 72 -7.5; 79 -8.3; 87 -9.0; 96 -9.4; 106 -9.5; 116 -9.3; 128 -9.2; 141 -9.0; 155 -8.7; 170 -8.4; 187 -8.3; 206 -8.0; 227 -7.5; 249 -7.2; 274 -7.3; 302 -7.1; 332 -6.9; 365 -6.8; 402 -6.6; 442 -6.3; 486 -6.3; 535 -6.3; 588 -6.0; 647 -5.9; 712 -6.0; 783 -5.9; 861 -6.2; 947 -6.4; 1042 -6.7; 1146 -6.9; 1261 -7.6; 1387 -8.7; 1526 -10.2; 1678 -10.9; 1846 -11.9; 2031 -15.0; 2234 -14.3; 2457 -12.5; 2703 -11.5; 2973 -10.0; 3270 -9.0; 3597 -7.9; 3957 -5.5; 4353 -4.4; 4788 -5.3; 5267 -9.5; 5793 -7.1; 6373 -7.5; 7010 -9.2; 7711 -10.1; 8482 -13.8; 9330 -15.1; 10263 -8.0; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado HF-2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado HF-2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 33 Hz    | 0.5  | 7.6 dB   |
| Peaking | 91 Hz    | 0.79 | -6.0 dB  |
| Peaking | 2138 Hz  | 2.28 | -8.6 dB  |
| Peaking | 9062 Hz  | 3.19 | -10.6 dB |
| Peaking | 10606 Hz | 2.82 | 3.2 dB   |
| Peaking | 704 Hz   | 0.91 | 1.5 dB   |
| Peaking | 1354 Hz  | 0.16 | -0.6 dB  |
| Peaking | 3284 Hz  | 3.38 | -1.5 dB  |
| Peaking | 4506 Hz  | 2.52 | 4.5 dB   |
| Peaking | 5276 Hz  | 7.92 | -4.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 8.1 dB  |
| Peaking | 62 Hz    | 1.41 | -0.7 dB |
| Peaking | 125 Hz   | 1.41 | -3.5 dB |
| Peaking | 250 Hz   | 1.41 | -0.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -8.4 dB |
| Peaking | 4000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.7 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20HF-2/Grado%20HF-2.png)