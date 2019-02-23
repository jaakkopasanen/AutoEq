# Kennerton Magister
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.1; 25 -1.6; 28 -2.2; 31 -2.6; 34 -3.0; 37 -3.2; 41 -3.4; 45 -3.4; 49 -3.5; 54 -3.8; 60 -4.3; 66 -4.4; 72 -4.4; 79 -4.5; 87 -5.7; 96 -6.2; 106 -7.2; 116 -8.0; 128 -8.6; 141 -8.9; 155 -8.7; 170 -8.1; 187 -9.0; 206 -8.8; 227 -8.3; 249 -7.6; 274 -6.4; 302 -4.7; 332 -3.4; 365 -2.9; 402 -3.6; 442 -4.3; 486 -5.1; 535 -5.6; 588 -5.8; 647 -6.3; 712 -6.4; 783 -6.2; 861 -6.3; 947 -6.9; 1042 -7.0; 1146 -7.3; 1261 -7.9; 1387 -9.0; 1526 -10.0; 1678 -10.8; 1846 -11.5; 2031 -11.0; 2234 -10.8; 2457 -9.7; 2703 -9.0; 2973 -7.8; 3270 -7.4; 3597 -6.9; 3957 -7.0; 4353 -6.2; 4788 -4.9; 5267 -1.0; 5793 -0.7; 6373 -2.2; 7010 -4.3; 7711 -6.3; 8482 -6.6; 9330 -6.6; 10263 -6.6; 11289 -6.6; 12418 -6.6; 13660 -6.6; 15026 -6.6; 16529 -6.6; 18182 -6.6; 20000 -6.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Kennerton Magister GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Kennerton Magister ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 1.33 | 5.9 dB  |
| Peaking | 50 Hz   | 2.18 | 2.5 dB  |
| Peaking | 379 Hz  | 3.36 | 4.1 dB  |
| Peaking | 1946 Hz | 1.66 | -5.1 dB |
| Peaking | 5735 Hz | 3.45 | 7.0 dB  |
| Peaking | 78 Hz   | 2.06 | 2.7 dB  |
| Peaking | 181 Hz  | 0.49 | -3.0 dB |
| Peaking | 310 Hz  | 3.86 | 2.6 dB  |
| Peaking | 538 Hz  | 0.93 | 1.5 dB  |
| Peaking | 8311 Hz | 5.21 | -0.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.5 dB  |
| Peaking | 62 Hz    | 1.41 | 2.6 dB  |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | -0.3 dB |
| Peaking | 500 Hz   | 1.41 | 2.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.0 dB |
| Peaking | 2000 Hz  | 1.41 | -5.6 dB |
| Peaking | 4000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Kennerton%20Magister/Kennerton%20Magister.png)