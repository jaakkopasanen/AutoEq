# Denon AH-D2000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.7; 45 -0.9; 49 -1.0; 54 -1.0; 60 -0.9; 66 -1.2; 72 -1.5; 79 -1.7; 87 -1.9; 96 -2.2; 106 -2.3; 116 -2.4; 128 -2.7; 141 -2.9; 155 -3.0; 170 -3.0; 187 -2.9; 206 -3.1; 227 -3.1; 249 -3.1; 274 -3.2; 302 -3.2; 332 -3.4; 365 -3.6; 402 -3.9; 442 -4.3; 486 -5.0; 535 -5.6; 588 -5.8; 647 -6.2; 712 -6.7; 783 -5.1; 861 -6.3; 947 -6.6; 1042 -6.4; 1146 -6.1; 1261 -5.9; 1387 -5.9; 1526 -5.9; 1678 -5.6; 1846 -5.3; 2031 -4.7; 2234 -4.3; 2457 -3.7; 2703 -3.3; 2973 -1.1; 3270 -1.3; 3597 -3.8; 3957 -4.4; 4353 -4.3; 4788 -3.8; 5267 -3.3; 5793 -4.3; 6373 -5.2; 7010 -5.5; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-D2000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D2000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.17 | 6.0 dB  |
| Peaking | 283 Hz  | 2.92 | -1.3 dB |
| Peaking | 291 Hz  | 1.4  | 3.3 dB  |
| Peaking | 3025 Hz | 2.26 | 5.0 dB  |
| Peaking | 5313 Hz | 3.27 | 2.7 dB  |
| Peaking | 678 Hz  | 7.52 | -0.8 dB |
| Peaking | 2058 Hz | 6.42 | 0.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 4.0 dB  |
| Peaking | 125 Hz   | 1.41 | 2.6 dB  |
| Peaking | 250 Hz   | 1.41 | 3.0 dB  |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.8 dB |
| Peaking | 2000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-D2000/Denon%20AH-D2000.png)