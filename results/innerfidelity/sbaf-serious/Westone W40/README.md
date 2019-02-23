# Westone W40
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.4; 23 -3.0; 25 -3.5; 28 -4.2; 31 -4.7; 34 -5.2; 37 -5.6; 41 -6.1; 45 -6.5; 49 -6.9; 54 -7.4; 60 -7.9; 66 -8.4; 72 -8.9; 79 -9.3; 87 -9.9; 96 -10.4; 106 -10.8; 116 -11.0; 128 -11.4; 141 -11.7; 155 -11.9; 170 -12.1; 187 -12.2; 206 -12.2; 227 -12.1; 249 -12.1; 274 -11.9; 302 -11.7; 332 -11.4; 365 -11.2; 402 -10.8; 442 -10.3; 486 -10.0; 535 -9.4; 588 -8.6; 647 -8.1; 712 -7.6; 783 -6.9; 861 -6.5; 947 -6.3; 1042 -6.3; 1146 -6.3; 1261 -6.4; 1387 -6.7; 1526 -6.8; 1678 -6.5; 1846 -5.5; 2031 -4.4; 2234 -3.2; 2457 -1.9; 2703 -0.9; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.7; 9330 -10.2; 10263 -9.5; 11289 -6.6; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Westone W40 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone W40 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 17 Hz   | 0.86 | 4.7 dB  |
| Peaking | 105 Hz  | 0.85 | -2.1 dB |
| Peaking | 250 Hz  | 0.55 | -5.2 dB |
| Peaking | 4393 Hz | 0.69 | 7.1 dB  |
| Peaking | 9354 Hz | 2.45 | -6.4 dB |
| Peaking | 880 Hz  | 2.55 | 1.0 dB  |
| Peaking | 1636 Hz | 2.33 | -1.8 dB |
| Peaking | 2742 Hz | 2.08 | 2.5 dB  |
| Peaking | 3815 Hz | 0.8  | -1.3 dB |
| Peaking | 6104 Hz | 5.11 | 1.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.9 dB  |
| Peaking | 62 Hz    | 1.41 | -1.5 dB |
| Peaking | 125 Hz   | 1.41 | -4.2 dB |
| Peaking | 250 Hz   | 1.41 | -5.1 dB |
| Peaking | 500 Hz   | 1.41 | -2.4 dB |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Westone%20W40/Westone%20W40.png)