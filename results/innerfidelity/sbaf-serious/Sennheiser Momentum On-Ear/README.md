# Sennheiser Momentum On-Ear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.4; 23 -9.6; 25 -9.7; 28 -9.8; 31 -10.0; 34 -10.1; 37 -10.2; 41 -10.3; 45 -10.3; 49 -10.4; 54 -10.4; 60 -10.5; 66 -10.4; 72 -10.3; 79 -10.4; 87 -10.5; 96 -10.5; 106 -10.5; 116 -10.4; 128 -10.5; 141 -10.4; 155 -10.1; 170 -9.6; 187 -9.2; 206 -8.7; 227 -7.9; 249 -7.0; 274 -6.1; 302 -5.2; 332 -4.7; 365 -4.4; 402 -4.3; 442 -4.0; 486 -4.3; 535 -4.6; 588 -4.9; 647 -5.5; 712 -6.1; 783 -6.0; 861 -5.8; 947 -5.7; 1042 -6.1; 1146 -7.0; 1261 -8.0; 1387 -9.2; 1526 -10.3; 1678 -11.1; 1846 -11.3; 2031 -10.3; 2234 -9.2; 2457 -7.3; 2703 -5.4; 2973 -3.8; 3270 -2.6; 3597 -1.1; 3957 -0.5; 4353 -0.5; 4788 -4.7; 5267 -4.4; 5793 -3.1; 6373 -4.7; 7010 -6.6; 7711 -6.9; 8482 -7.9; 9330 -8.3; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Momentum On-Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum On-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 44 Hz   | 0.6  | -4.1 dB |
| Peaking | 131 Hz  | 1.72 | -3.2 dB |
| Peaking | 1820 Hz | 2.41 | -5.8 dB |
| Peaking | 3242 Hz | 2.6  | 2.0 dB  |
| Peaking | 4038 Hz | 2.38 | 5.7 dB  |
| Peaking | 16 Hz   | 1.83 | -1.4 dB |
| Peaking | 347 Hz  | 3.43 | 1.6 dB  |
| Peaking | 489 Hz  | 1.8  | 2.4 dB  |
| Peaking | 5934 Hz | 8.75 | 2.5 dB  |
| Peaking | 8837 Hz | 3.91 | -2.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.5 dB |
| Peaking | 62 Hz    | 1.41 | -2.8 dB |
| Peaking | 125 Hz   | 1.41 | -4.0 dB |
| Peaking | 250 Hz   | 1.41 | -0.0 dB |
| Peaking | 500 Hz   | 1.41 | 2.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.6 dB |
| Peaking | 4000 Hz  | 1.41 | 7.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20Momentum%20On-Ear/Sennheiser%20Momentum%20On-Ear.png)