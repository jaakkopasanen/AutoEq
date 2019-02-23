# Fidue A63
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.4; 23 -4.8; 25 -5.2; 28 -5.9; 31 -6.6; 34 -7.1; 37 -7.5; 41 -8.0; 45 -8.5; 49 -8.9; 54 -9.3; 60 -9.7; 66 -10.2; 72 -10.6; 79 -11.1; 87 -11.4; 96 -11.9; 106 -12.1; 116 -12.3; 128 -12.4; 141 -12.6; 155 -12.6; 170 -12.5; 187 -12.2; 206 -12.1; 227 -11.6; 249 -11.3; 274 -10.9; 302 -10.4; 332 -9.9; 365 -9.3; 402 -8.8; 442 -8.0; 486 -7.6; 535 -7.0; 588 -6.1; 647 -5.6; 712 -5.5; 783 -5.0; 861 -4.8; 947 -4.2; 1042 -4.4; 1146 -5.0; 1261 -5.7; 1387 -6.5; 1526 -7.2; 1678 -7.6; 1846 -7.6; 2031 -7.4; 2234 -7.1; 2457 -6.4; 2703 -5.3; 2973 -3.5; 3270 -1.4; 3597 -0.5; 3957 -0.5; 4353 -1.6; 4788 -1.9; 5267 -1.0; 5793 -1.0; 6373 -1.1; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fidue A63 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fidue A63 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 1.99 | 2.7 dB  |
| Peaking | 107 Hz  | 0.69 | -5.4 dB |
| Peaking | 230 Hz  | 1.32 | -3.3 dB |
| Peaking | 3689 Hz | 2.87 | 6.0 dB  |
| Peaking | 5739 Hz | 2.73 | 5.5 dB  |
| Peaking | 383 Hz  | 2.33 | -1.0 dB |
| Peaking | 1020 Hz | 1.03 | 3.7 dB  |
| Peaking | 1800 Hz | 0.92 | -3.8 dB |
| Peaking | 2904 Hz | 1    | 1.6 dB  |
| Peaking | 8239 Hz | 4.11 | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.1 dB  |
| Peaking | 62 Hz    | 1.41 | -3.0 dB |
| Peaking | 125 Hz   | 1.41 | -5.3 dB |
| Peaking | 250 Hz   | 1.41 | -4.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.1 dB |
| Peaking | 4000 Hz  | 1.41 | 7.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fidue%20A63/Fidue%20A63.png)