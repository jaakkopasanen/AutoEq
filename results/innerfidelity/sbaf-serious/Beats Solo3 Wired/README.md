# Beats Solo3 Wired
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.0; 23 -9.2; 25 -9.3; 28 -9.4; 31 -9.4; 34 -9.5; 37 -9.6; 41 -9.5; 45 -9.6; 49 -9.7; 54 -9.7; 60 -9.8; 66 -10.0; 72 -10.0; 79 -10.3; 87 -10.4; 96 -10.7; 106 -11.1; 116 -11.0; 128 -11.0; 141 -11.2; 155 -11.3; 170 -11.0; 187 -11.2; 206 -10.9; 227 -10.4; 249 -10.0; 274 -9.2; 302 -8.5; 332 -7.7; 365 -7.0; 402 -5.9; 442 -5.3; 486 -5.2; 535 -4.7; 588 -3.7; 647 -3.2; 712 -2.8; 783 -2.5; 861 -2.8; 947 -3.0; 1042 -3.2; 1146 -3.5; 1261 -3.8; 1387 -4.3; 1526 -4.6; 1678 -4.9; 1846 -4.7; 2031 -4.2; 2234 -4.1; 2457 -3.9; 2703 -4.4; 2973 -4.9; 3270 -5.6; 3597 -5.7; 3957 -3.5; 4353 -5.0; 4788 -5.2; 5267 -2.4; 5793 -0.5; 6373 -1.6; 7010 -3.0; 7711 -5.2; 8482 -5.4; 9330 -5.5; 10263 -5.5; 11289 -5.5; 12418 -5.5; 13660 -5.5; 15026 -5.5; 16529 -5.5; 18182 -5.5; 20000 -5.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats Solo3 Wired GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Solo3 Wired ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.4  | -3.5 dB |
| Peaking | 112 Hz  | 0.81 | -2.8 dB |
| Peaking | 215 Hz  | 0.86 | -4.1 dB |
| Peaking | 767 Hz  | 0.8  | 3.2 dB  |
| Peaking | 5963 Hz | 3.74 | 5.2 dB  |
| Peaking | 1606 Hz | 1.81 | -1.4 dB |
| Peaking | 2937 Hz | 0.71 | 2.3 dB  |
| Peaking | 3821 Hz | 1.8  | -3.9 dB |
| Peaking | 3993 Hz | 7.99 | 3.8 dB  |
| Peaking | 8314 Hz | 5.14 | -0.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.9 dB |
| Peaking | 62 Hz    | 1.41 | -3.0 dB |
| Peaking | 125 Hz   | 1.41 | -4.9 dB |
| Peaking | 250 Hz   | 1.41 | -4.3 dB |
| Peaking | 500 Hz   | 1.41 | 1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beats%20Solo3%20Wired/Beats%20Solo3%20Wired.png)