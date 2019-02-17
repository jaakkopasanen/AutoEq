# Yamaha HP1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.1; 23 -1.5; 25 -1.9; 28 -2.5; 31 -2.9; 34 -3.2; 37 -3.5; 41 -3.8; 45 -4.0; 49 -4.2; 54 -4.5; 60 -4.7; 66 -4.9; 72 -5.2; 79 -5.4; 87 -5.6; 96 -6.0; 106 -6.4; 116 -6.5; 128 -6.9; 141 -7.2; 155 -7.3; 170 -7.4; 187 -7.6; 206 -7.7; 227 -7.6; 249 -7.7; 274 -7.5; 302 -7.4; 332 -7.5; 365 -7.4; 402 -7.5; 442 -7.3; 486 -7.5; 535 -7.6; 588 -7.3; 647 -7.3; 712 -7.5; 783 -7.1; 861 -7.0; 947 -6.6; 1042 -6.1; 1146 -5.3; 1261 -4.1; 1387 -3.6; 1526 -3.7; 1678 -3.2; 1846 -3.3; 2031 -4.4; 2234 -5.9; 2457 -5.1; 2703 -5.2; 2973 -3.5; 3270 -1.9; 3597 -1.3; 3957 -1.9; 4353 -2.9; 4788 -1.8; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Yamaha HP1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yamaha HP1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 1.19 | 5.2 dB  |
| Peaking | 50 Hz   | 1.82 | 1.6 dB  |
| Peaking | 1605 Hz | 2.62 | 3.4 dB  |
| Peaking | 3574 Hz | 3.05 | 4.7 dB  |
| Peaking | 5653 Hz | 2.71 | 6.2 dB  |
| Peaking | 81 Hz   | 2.14 | 0.7 dB  |
| Peaking | 202 Hz  | 0.77 | -1.2 dB |
| Peaking | 655 Hz  | 0.95 | -0.9 dB |
| Peaking | 1257 Hz | 5.44 | 1.4 dB  |
| Peaking | 8209 Hz | 4.73 | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.3 dB  |
| Peaking | 62 Hz    | 1.41 | 1.2 dB  |
| Peaking | 125 Hz   | 1.41 | -0.6 dB |
| Peaking | 250 Hz   | 1.41 | -1.0 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Yamaha%20HP1/Yamaha%20HP1.png)