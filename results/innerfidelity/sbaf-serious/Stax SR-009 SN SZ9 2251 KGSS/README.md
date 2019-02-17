# Stax SR-009 SN SZ9 2251 KGSS
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -1.0; 66 -1.0; 72 -1.8; 79 -2.1; 87 -2.1; 96 -2.3; 106 -2.4; 116 -2.5; 128 -2.8; 141 -3.0; 155 -3.2; 170 -3.4; 187 -3.4; 206 -3.6; 227 -3.5; 249 -3.7; 274 -3.7; 302 -3.7; 332 -3.8; 365 -4.0; 402 -4.1; 442 -4.1; 486 -4.5; 535 -4.7; 588 -4.7; 647 -5.0; 712 -5.5; 783 -5.5; 861 -5.6; 947 -6.2; 1042 -6.5; 1146 -6.9; 1261 -7.0; 1387 -7.1; 1526 -7.1; 1678 -7.5; 1846 -5.2; 2031 -3.4; 2234 -2.6; 2457 -1.7; 2703 -3.5; 2973 -3.2; 3270 -3.3; 3597 -2.8; 3957 -4.0; 4353 -5.7; 4788 -7.0; 5267 -5.8; 5793 -0.7; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-009 SN SZ9 2251 KGSS GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-009 SN SZ9 2251 KGSS ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 112 Hz   |  0.09 | 8.3 dB  |
| Peaking | 540 Hz   |  0.1  | -5.3 dB |
| Peaking | 2370 Hz  |  2.38 | 6.8 dB  |
| Peaking | 3543 Hz  |  3.24 | 5.0 dB  |
| Peaking | 6166 Hz  |  3.89 | 7.8 dB  |
| Peaking | 54 Hz    |  3.66 | 0.5 dB  |
| Peaking | 1636 Hz  |  9.03 | -1.3 dB |
| Peaking | 3914 Hz  |  0.14 | 0.2 dB  |
| Peaking | 4965 Hz  | 10.79 | -1.8 dB |
| Peaking | 11133 Hz |  2.44 | 0.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.4 dB  |
| Peaking | 62 Hz    | 1.41 | 4.1 dB  |
| Peaking | 125 Hz   | 1.41 | 2.6 dB  |
| Peaking | 250 Hz   | 1.41 | 2.1 dB  |
| Peaking | 500 Hz   | 1.41 | 2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.4 dB |
| Peaking | 2000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-009%20SN%20SZ9%202251%20KGSS/Stax%20SR-009%20SN%20SZ9%202251%20KGSS.png)