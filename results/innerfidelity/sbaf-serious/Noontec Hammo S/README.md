# Noontec Hammo S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.7; 23 -5.9; 25 -6.0; 28 -6.3; 31 -6.4; 34 -6.6; 37 -6.7; 41 -6.8; 45 -6.8; 49 -7.0; 54 -7.1; 60 -7.2; 66 -7.3; 72 -7.4; 79 -7.4; 87 -7.6; 96 -7.4; 106 -7.0; 116 -6.9; 128 -7.8; 141 -8.9; 155 -9.6; 170 -8.3; 187 -9.3; 206 -9.2; 227 -9.0; 249 -8.4; 274 -7.8; 302 -7.1; 332 -6.4; 365 -5.6; 402 -4.9; 442 -4.6; 486 -4.4; 535 -4.3; 588 -4.6; 647 -5.5; 712 -6.0; 783 -5.6; 861 -5.5; 947 -5.8; 1042 -6.8; 1146 -7.5; 1261 -8.2; 1387 -8.7; 1526 -9.0; 1678 -9.1; 1846 -8.7; 2031 -7.8; 2234 -6.8; 2457 -5.1; 2703 -4.1; 2973 -3.1; 3270 -3.6; 3597 -7.0; 3957 -5.2; 4353 -6.5; 4788 -3.2; 5267 -0.6; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -7.4; 10263 -6.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Noontec Hammo S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noontec Hammo S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 223 Hz  | 0.82 | -4.2 dB |
| Peaking | 428 Hz  | 0.8  | 3.7 dB  |
| Peaking | 1598 Hz | 1.54 | -3.3 dB |
| Peaking | 2865 Hz | 3.74 | 3.8 dB  |
| Peaking | 5761 Hz | 3.25 | 6.9 dB  |
| Peaking | 18 Hz   | 1.86 | 0.9 dB  |
| Peaking | 150 Hz  | 9.6  | -0.7 dB |
| Peaking | 691 Hz  | 8.19 | -0.9 dB |
| Peaking | 889 Hz  | 5.21 | 0.7 dB  |
| Peaking | 9278 Hz | 4.08 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.3 dB  |
| Peaking | 62 Hz    | 1.41 | -0.5 dB |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | 3.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.8 dB |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB |
| Peaking | 4000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Noontec%20Hammo%20S/Noontec%20Hammo%20S.png)