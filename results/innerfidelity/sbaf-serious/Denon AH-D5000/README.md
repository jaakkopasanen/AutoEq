# Denon AH-D5000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.8; 28 -1.9; 31 -3.1; 34 -4.2; 37 -4.9; 41 -5.4; 45 -5.7; 49 -6.0; 54 -6.1; 60 -6.0; 66 -6.0; 72 -6.2; 79 -6.3; 87 -6.2; 96 -6.2; 106 -6.2; 116 -6.2; 128 -6.3; 141 -6.4; 155 -6.4; 170 -6.3; 187 -6.2; 206 -6.0; 227 -5.8; 249 -5.6; 274 -5.4; 302 -5.2; 332 -4.8; 365 -4.5; 402 -4.3; 442 -3.9; 486 -4.2; 535 -4.8; 588 -5.6; 647 -6.8; 712 -8.0; 783 -8.9; 861 -9.7; 947 -7.5; 1042 -7.4; 1146 -7.7; 1261 -7.1; 1387 -6.7; 1526 -6.5; 1678 -5.9; 1846 -5.2; 2031 -4.5; 2234 -4.1; 2457 -4.6; 2703 -5.6; 2973 -6.7; 3270 -7.4; 3597 -7.9; 3957 -6.8; 4353 -6.2; 4788 -4.8; 5267 -3.6; 5793 -5.1; 6373 -5.9; 7010 -5.4; 7711 -6.2; 8482 -6.5; 9330 -9.0; 10263 -9.5; 11289 -8.5; 12418 -8.0; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.7; 20000 -8.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-D5000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D5000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 1.61 | 6.5 dB  |
| Peaking | 459 Hz   | 1.21 | 3.0 dB  |
| Peaking | 804 Hz   | 2.1  | -3.7 dB |
| Peaking | 2193 Hz  | 3.51 | 2.7 dB  |
| Peaking | 10264 Hz | 3.98 | -3.5 dB |
| Peaking | 29 Hz    | 0.98 | -0.6 dB |
| Peaking | 1169 Hz  | 8.84 | -0.6 dB |
| Peaking | 3536 Hz  | 3.98 | -1.9 dB |
| Peaking | 5263 Hz  | 3.16 | 2.8 dB  |
| Peaking | 12035 Hz | 7.26 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.2 dB  |
| Peaking | 62 Hz    | 1.41 | -0.6 dB |
| Peaking | 125 Hz   | 1.41 | -0.1 dB |
| Peaking | 250 Hz   | 1.41 | 0.7 dB  |
| Peaking | 500 Hz   | 1.41 | 2.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.1 dB |
| Peaking | 2000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-D5000/Denon%20AH-D5000.png)