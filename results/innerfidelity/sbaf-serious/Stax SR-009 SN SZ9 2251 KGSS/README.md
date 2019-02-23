# Stax SR-009 SN SZ9 2251 KGSS
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.7; 23 -0.7; 25 -0.7; 28 -0.7; 31 -0.6; 34 -0.6; 37 -0.6; 41 -0.8; 45 -1.0; 49 -1.2; 54 -2.0; 60 -2.9; 66 -3.0; 72 -3.8; 79 -4.1; 87 -4.1; 96 -4.3; 106 -4.4; 116 -4.5; 128 -4.8; 141 -5.0; 155 -5.2; 170 -5.4; 187 -5.4; 206 -5.6; 227 -5.5; 249 -5.7; 274 -5.7; 302 -5.7; 332 -5.8; 365 -6.0; 402 -6.1; 442 -6.0; 486 -6.5; 535 -6.7; 588 -6.7; 647 -7.0; 712 -7.5; 783 -7.5; 861 -7.6; 947 -8.2; 1042 -8.5; 1146 -8.9; 1261 -9.0; 1387 -9.1; 1526 -9.1; 1678 -9.5; 1846 -7.2; 2031 -5.4; 2234 -4.6; 2457 -3.7; 2703 -5.4; 2973 -5.2; 3270 -5.3; 3597 -4.8; 3957 -6.0; 4353 -7.7; 4788 -9.0; 5267 -7.8; 5793 -1.2; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -5.9; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-009 SN SZ9 2251 KGSS GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-009 SN SZ9 2251 KGSS ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.51 | 5.6 dB  |
| Peaking | 1629 Hz | 0.95 | -6.1 dB |
| Peaking | 2255 Hz | 1.4  | 5.8 dB  |
| Peaking | 5007 Hz | 4.14 | -5.2 dB |
| Peaking | 6119 Hz | 4.19 | 7.6 dB  |
| Peaking | 2533 Hz | 7.16 | 1.3 dB  |
| Peaking | 2712 Hz | 6.11 | -1.7 dB |
| Peaking | 3601 Hz | 8.95 | 1.3 dB  |
| Peaking | 7987 Hz | 5.65 | -0.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 1.9 dB  |
| Peaking | 125 Hz   | 1.41 | 0.6 dB  |
| Peaking | 250 Hz   | 1.41 | 0.2 dB  |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.3 dB |
| Peaking | 2000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.1 dB |
| Peaking | 8000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-009%20SN%20SZ9%202251%20KGSS/Stax%20SR-009%20SN%20SZ9%202251%20KGSS.png)