# Stax SR-009 SZ9-1278
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -1.5; 66 -2.0; 72 -1.6; 79 -1.5; 87 -1.7; 96 -2.0; 106 -2.1; 116 -2.3; 128 -2.6; 141 -2.7; 155 -2.9; 170 -3.2; 187 -3.2; 206 -3.4; 227 -3.4; 249 -3.5; 274 -3.5; 302 -3.6; 332 -3.6; 365 -3.7; 402 -3.8; 442 -3.9; 486 -4.4; 535 -4.5; 588 -4.4; 647 -4.6; 712 -5.0; 783 -4.9; 861 -5.0; 947 -5.9; 1042 -6.5; 1146 -6.6; 1261 -6.6; 1387 -6.7; 1526 -6.6; 1678 -6.9; 1846 -5.2; 2031 -3.7; 2234 -3.3; 2457 -2.4; 2703 -2.4; 2973 -3.1; 3270 -3.2; 3597 -2.4; 3957 -3.7; 4353 -5.1; 4788 -6.7; 5267 -3.9; 5793 -0.5; 6373 -1.1; 7010 -4.1; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-009 SZ9-1278 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-009 SZ9-1278 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 92 Hz   | 0.09 | 7.4 dB  |
| Peaking | 591 Hz  | 0.1  | -4.1 dB |
| Peaking | 2820 Hz | 1.23 | 6.7 dB  |
| Peaking | 6068 Hz | 3.9  | 7.1 dB  |
| Peaking | 1699 Hz | 2.77 | -1.4 dB |
| Peaking | 1995 Hz | 5.03 | 1.4 dB  |
| Peaking | 3008 Hz | 4.12 | -3.0 dB |
| Peaking | 3484 Hz | 1.58 | 2.4 dB  |
| Peaking | 4803 Hz | 6.87 | -2.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 3.8 dB  |
| Peaking | 125 Hz   | 1.41 | 3.0 dB  |
| Peaking | 250 Hz   | 1.41 | 2.1 dB  |
| Peaking | 500 Hz   | 1.41 | 2.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.8 dB |
| Peaking | 2000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-009%20SZ9-1278/Stax%20SR-009%20SZ9-1278.png)