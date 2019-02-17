# Noontec Zoro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.5; 23 -6.9; 25 -7.2; 28 -7.5; 31 -7.8; 34 -8.0; 37 -8.2; 41 -8.4; 45 -8.6; 49 -8.7; 54 -8.9; 60 -9.1; 66 -9.3; 72 -9.6; 79 -9.9; 87 -10.2; 96 -10.4; 106 -10.7; 116 -10.8; 128 -11.0; 141 -11.1; 155 -11.2; 170 -11.2; 187 -11.2; 206 -11.2; 227 -11.2; 249 -11.0; 274 -10.7; 302 -10.4; 332 -10.4; 365 -10.3; 402 -10.0; 442 -9.7; 486 -9.8; 535 -9.5; 588 -9.0; 647 -8.6; 712 -8.1; 783 -7.3; 861 -6.8; 947 -6.5; 1042 -6.5; 1146 -6.6; 1261 -6.6; 1387 -7.5; 1526 -8.3; 1678 -8.0; 1846 -7.1; 2031 -5.3; 2234 -3.4; 2457 -1.0; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.8; 6373 -2.2; 7010 -4.2; 7711 -7.9; 8482 -8.8; 9330 -6.8; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Noontec Zoro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noontec Zoro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 92 Hz    | 0.45 | -1.8 dB |
| Peaking | 275 Hz   | 0.35 | -3.8 dB |
| Peaking | 1664 Hz  | 2    | -6.1 dB |
| Peaking | 3343 Hz  | 0.46 | 7.5 dB  |
| Peaking | 8313 Hz  | 2.87 | -5.9 dB |
| Peaking | 931 Hz   | 3.35 | 0.5 dB  |
| Peaking | 2574 Hz  | 6.8  | 1.4 dB  |
| Peaking | 3846 Hz  | 1.06 | -0.9 dB |
| Peaking | 5710 Hz  | 2.33 | 1.6 dB  |
| Peaking | 12644 Hz | 1.5  | -0.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.8 dB |
| Peaking | 62 Hz    | 1.41 | -2.0 dB |
| Peaking | 125 Hz   | 1.41 | -3.8 dB |
| Peaking | 250 Hz   | 1.41 | -3.7 dB |
| Peaking | 500 Hz   | 1.41 | -2.5 dB |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | -0.1 dB |
| Peaking | 4000 Hz  | 1.41 | 8.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Noontec%20Zoro/Noontec%20Zoro.png)