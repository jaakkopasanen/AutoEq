# Klipsch Image One
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.4; 25 -2.2; 28 -3.2; 31 -4.1; 34 -4.8; 37 -5.4; 41 -6.2; 45 -6.8; 49 -7.4; 54 -8.0; 60 -8.5; 66 -8.8; 72 -9.1; 79 -9.6; 87 -10.1; 96 -10.6; 106 -10.8; 116 -11.2; 128 -11.2; 141 -11.4; 155 -11.6; 170 -11.6; 187 -11.8; 206 -11.5; 227 -11.1; 249 -10.7; 274 -10.4; 302 -10.2; 332 -10.0; 365 -9.5; 402 -9.3; 442 -9.2; 486 -8.7; 535 -7.9; 588 -6.9; 647 -5.8; 712 -5.4; 783 -5.9; 861 -6.6; 947 -7.4; 1042 -6.7; 1146 -8.3; 1261 -9.0; 1387 -9.7; 1526 -10.2; 1678 -10.9; 1846 -11.6; 2031 -12.0; 2234 -12.3; 2457 -12.8; 2703 -13.8; 2973 -13.5; 3270 -12.0; 3597 -9.4; 3957 -6.4; 4353 -5.5; 4788 -5.7; 5267 -5.8; 5793 -6.8; 6373 -6.6; 7010 -7.7; 7711 -6.7; 8482 -6.9; 9330 -7.0; 10263 -7.0; 11289 -7.0; 12418 -7.0; 13660 -7.0; 15026 -7.0; 16529 -7.0; 18182 -7.0; 20000 -7.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Klipsch Image One GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch Image One ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 1.12 | 6.9 dB  |
| Peaking | 112 Hz  | 0.73 | -3.7 dB |
| Peaking | 231 Hz  | 1.14 | -2.7 dB |
| Peaking | 2792 Hz | 1.15 | -8.2 dB |
| Peaking | 4230 Hz | 1.91 | 5.4 dB  |
| Peaking | 491 Hz  | 1.66 | -2.4 dB |
| Peaking | 672 Hz  | 1.42 | 3.5 dB  |
| Peaking | 2082 Hz | 0.89 | -2.1 dB |
| Peaking | 2368 Hz | 3.05 | 2.2 dB  |
| Peaking | 4518 Hz | 0.52 | 0.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.3 dB  |
| Peaking | 62 Hz    | 1.41 | -2.0 dB |
| Peaking | 125 Hz   | 1.41 | -3.9 dB |
| Peaking | 250 Hz   | 1.41 | -3.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.0 dB |
| Peaking | 4000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Klipsch%20Image%20One/Klipsch%20Image%20One.png)