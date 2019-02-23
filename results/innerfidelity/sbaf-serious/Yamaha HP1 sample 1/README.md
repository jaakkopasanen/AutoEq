# Yamaha HP1 sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.9; 23 -3.4; 25 -3.9; 28 -4.4; 31 -4.8; 34 -5.2; 37 -5.4; 41 -5.7; 45 -5.9; 49 -6.0; 54 -6.2; 60 -6.6; 66 -6.9; 72 -7.1; 79 -7.4; 87 -7.6; 96 -8.0; 106 -8.2; 116 -8.3; 128 -8.7; 141 -8.9; 155 -9.1; 170 -9.3; 187 -9.3; 206 -9.5; 227 -9.4; 249 -9.5; 274 -9.3; 302 -9.3; 332 -9.2; 365 -9.1; 402 -9.2; 442 -8.9; 486 -9.1; 535 -9.1; 588 -8.7; 647 -8.8; 712 -8.9; 783 -8.5; 861 -8.5; 947 -8.4; 1042 -8.1; 1146 -7.4; 1261 -6.2; 1387 -5.8; 1526 -6.0; 1678 -5.2; 1846 -5.1; 2031 -6.3; 2234 -8.1; 2457 -6.6; 2703 -7.6; 2973 -4.9; 3270 -3.2; 3597 -2.3; 3957 -3.2; 4353 -4.8; 4788 -3.8; 5267 -0.7; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -7.9; 20000 -9.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Yamaha HP1 sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yamaha HP1 sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 13 Hz   | 0.22 | 4.9 dB  |
| Peaking | 409 Hz  | 0.05 | -3.1 dB |
| Peaking | 1571 Hz | 1.49 | 3.9 dB  |
| Peaking | 3552 Hz | 3.48 | 5.6 dB  |
| Peaking | 5802 Hz | 2.42 | 8.1 dB  |
| Peaking | 198 Hz  | 0.86 | -1.5 dB |
| Peaking | 208 Hz  | 0.49 | 1.1 dB  |
| Peaking | 2219 Hz | 7.44 | -0.9 dB |
| Peaking | 3026 Hz | 9.1  | 0.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.4 dB  |
| Peaking | 62 Hz    | 1.41 | -0.3 dB |
| Peaking | 125 Hz   | 1.41 | -1.9 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | -2.2 dB |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB |
| Peaking | 2000 Hz  | 1.41 | -0.4 dB |
| Peaking | 4000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Yamaha%20HP1%20sample%201/Yamaha%20HP1%20sample%201.png)