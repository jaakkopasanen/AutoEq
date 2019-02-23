# Westone W2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.9; 23 -5.0; 25 -5.1; 28 -5.2; 31 -5.3; 34 -5.4; 37 -5.5; 41 -5.7; 45 -5.9; 49 -6.0; 54 -6.2; 60 -6.5; 66 -6.9; 72 -7.3; 79 -7.6; 87 -8.1; 96 -8.5; 106 -8.8; 116 -9.0; 128 -9.4; 141 -9.6; 155 -9.9; 170 -10.1; 187 -10.2; 206 -10.2; 227 -10.2; 249 -10.1; 274 -10.1; 302 -10.0; 332 -9.8; 365 -9.6; 402 -9.4; 442 -9.1; 486 -8.8; 535 -8.4; 588 -7.9; 647 -7.6; 712 -7.5; 783 -7.0; 861 -7.3; 947 -7.6; 1042 -7.9; 1146 -8.1; 1261 -8.4; 1387 -9.0; 1526 -9.5; 1678 -9.9; 1846 -9.9; 2031 -9.6; 2234 -9.0; 2457 -7.2; 2703 -5.0; 2973 -1.6; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.7; 5267 -2.1; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Westone W2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone W2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.5  | 1.7 dB  |
| Peaking | 206 Hz  | 0.52 | -3.9 dB |
| Peaking | 2030 Hz | 1.3  | -5.8 dB |
| Peaking | 3475 Hz | 1.37 | 8.3 dB  |
| Peaking | 5999 Hz | 4.2  | 4.6 dB  |
| Peaking | 415 Hz  | 2.85 | -0.4 dB |
| Peaking | 770 Hz  | 2.98 | 0.7 dB  |
| Peaking | 1415 Hz | 5.18 | -0.4 dB |
| Peaking | 6634 Hz | 8.01 | 1.6 dB  |
| Peaking | 7947 Hz | 2.47 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.7 dB  |
| Peaking | 62 Hz    | 1.41 | 0.0 dB  |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | -3.5 dB |
| Peaking | 500 Hz   | 1.41 | -1.3 dB |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | -4.7 dB |
| Peaking | 4000 Hz  | 1.41 | 8.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Westone%20W2/Westone%20W2.png)