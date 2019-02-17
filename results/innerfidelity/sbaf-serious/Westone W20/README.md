# Westone W20
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.3; 23 -4.5; 25 -4.6; 28 -4.8; 31 -5.0; 34 -5.1; 37 -5.3; 41 -5.5; 45 -5.7; 49 -5.9; 54 -6.1; 60 -6.4; 66 -6.8; 72 -7.2; 79 -7.5; 87 -8.0; 96 -8.4; 106 -8.7; 116 -8.9; 128 -9.3; 141 -9.6; 155 -9.7; 170 -9.9; 187 -9.9; 206 -10.0; 227 -9.9; 249 -9.9; 274 -9.7; 302 -9.6; 332 -9.4; 365 -9.1; 402 -8.8; 442 -8.4; 486 -8.2; 535 -7.8; 588 -7.2; 647 -6.8; 712 -6.6; 783 -6.2; 861 -6.2; 947 -6.4; 1042 -6.6; 1146 -6.7; 1261 -6.9; 1387 -7.4; 1526 -7.9; 1678 -8.3; 1846 -8.3; 2031 -8.1; 2234 -7.8; 2457 -6.1; 2703 -3.9; 2973 -0.8; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.0; 5267 -2.2; 5793 -0.6; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Westone W20 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone W20 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.53 | 2.2 dB  |
| Peaking | 193 Hz  | 0.6  | -3.8 dB |
| Peaking | 2082 Hz | 1.77 | -4.5 dB |
| Peaking | 3478 Hz | 1.24 | 7.5 dB  |
| Peaking | 6037 Hz | 4.47 | 4.2 dB  |
| Peaking | 812 Hz  | 2.98 | 1.0 dB  |
| Peaking | 1533 Hz | 5.53 | -0.7 dB |
| Peaking | 3732 Hz | 4.81 | -1.9 dB |
| Peaking | 4008 Hz | 1.89 | 1.3 dB  |
| Peaking | 8404 Hz | 2.5  | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.1 dB  |
| Peaking | 62 Hz    | 1.41 | 0.0 dB  |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | -3.3 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.2 dB |
| Peaking | 4000 Hz  | 1.41 | 8.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Westone%20W20/Westone%20W20.png)