# Sennheiser IE 800 sample A
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.8; 23 -11.9; 25 -12.0; 28 -12.1; 31 -12.2; 34 -12.2; 37 -12.2; 41 -12.2; 45 -12.2; 49 -12.2; 54 -12.2; 60 -12.3; 66 -12.3; 72 -12.3; 79 -12.4; 87 -12.4; 96 -12.5; 106 -12.3; 116 -12.1; 128 -12.1; 141 -11.9; 155 -11.7; 170 -11.4; 187 -11.0; 206 -10.7; 227 -10.3; 249 -9.9; 274 -9.5; 302 -9.2; 332 -8.7; 365 -8.4; 402 -8.1; 442 -7.6; 486 -7.4; 535 -7.1; 588 -6.6; 647 -6.4; 712 -6.4; 783 -6.1; 861 -6.4; 947 -6.7; 1042 -7.0; 1146 -7.2; 1261 -7.4; 1387 -7.7; 1526 -7.9; 1678 -7.7; 1846 -6.8; 2031 -5.6; 2234 -4.1; 2457 -2.2; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -2.1; 4788 -4.9; 5267 -5.8; 5793 -4.6; 6373 -1.1; 7010 -4.0; 7711 -6.2; 8482 -6.8; 9330 -9.3; 10263 -10.0; 11289 -7.1; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser IE 800 sample A GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser IE 800 sample A ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.27 | -5.2 dB |
| Peaking | 146 Hz  | 0.57 | -3.5 dB |
| Peaking | 3298 Hz | 1.84 | 7.0 dB  |
| Peaking | 6473 Hz | 7.26 | 5.2 dB  |
| Peaking | 9928 Hz | 4.05 | -4.2 dB |
| Peaking | 714 Hz  | 2    | 1.0 dB  |
| Peaking | 1571 Hz | 1.78 | -2.1 dB |
| Peaking | 2590 Hz | 3.68 | 2.8 dB  |
| Peaking | 3865 Hz | 1.74 | -2.6 dB |
| Peaking | 4046 Hz | 5    | 4.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.7 dB |
| Peaking | 62 Hz    | 1.41 | -4.3 dB |
| Peaking | 125 Hz   | 1.41 | -4.7 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB |
| Peaking | 2000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20IE%20800%20sample%20A/Sennheiser%20IE%20800%20sample%20A.png)