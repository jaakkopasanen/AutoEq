# Denon AH-D600
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.3; 23 -10.5; 25 -10.6; 28 -10.6; 31 -10.7; 34 -10.7; 37 -10.6; 41 -10.5; 45 -10.4; 49 -10.2; 54 -9.8; 60 -9.6; 66 -9.9; 72 -10.7; 79 -11.3; 87 -11.6; 96 -11.9; 106 -12.0; 116 -12.0; 128 -12.1; 141 -12.0; 155 -11.6; 170 -10.6; 187 -10.2; 206 -8.7; 227 -6.5; 249 -4.7; 274 -4.3; 302 -5.3; 332 -6.1; 365 -6.2; 402 -6.3; 442 -5.5; 486 -6.1; 535 -6.6; 588 -6.6; 647 -6.5; 712 -6.7; 783 -6.3; 861 -6.4; 947 -6.4; 1042 -6.5; 1146 -6.7; 1261 -7.2; 1387 -8.1; 1526 -9.0; 1678 -9.5; 1846 -9.6; 2031 -8.8; 2234 -7.9; 2457 -8.2; 2703 -7.7; 2973 -6.6; 3270 -4.9; 3597 -2.7; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -3.1; 6373 -5.3; 7010 -4.0; 7711 -6.2; 8482 -7.5; 9330 -11.5; 10263 -7.2; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.9; 18182 -9.7; 20000 -10.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-D600 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.48 | -4.1 dB |
| Peaking | 121 Hz  | 1.52 | -5.3 dB |
| Peaking | 2036 Hz | 1.41 | -3.6 dB |
| Peaking | 4508 Hz | 1.65 | 7.2 dB  |
| Peaking | 9238 Hz | 6.02 | -6.2 dB |
| Peaking | 186 Hz  | 3.08 | -2.1 dB |
| Peaking | 260 Hz  | 3.14 | 3.7 dB  |
| Peaking | 448 Hz  | 6.18 | 1.0 dB  |
| Peaking | 1059 Hz | 1.77 | 0.7 dB  |
| Peaking | 1555 Hz | 4.6  | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.3 dB |
| Peaking | 62 Hz    | 1.41 | -1.9 dB |
| Peaking | 125 Hz   | 1.41 | -6.6 dB |
| Peaking | 250 Hz   | 1.41 | 2.0 dB  |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.9 dB |
| Peaking | 4000 Hz  | 1.41 | 7.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.3 dB |
| Peaking | 16000 Hz | 1.41 | -1.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-D600/Denon%20AH-D600.png)