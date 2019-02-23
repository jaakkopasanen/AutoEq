# NVX EX10S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.3; 23 -2.7; 25 -3.1; 28 -3.5; 31 -3.9; 34 -4.2; 37 -4.5; 41 -4.8; 45 -5.1; 49 -5.4; 54 -5.7; 60 -6.1; 66 -6.5; 72 -6.8; 79 -7.3; 87 -7.7; 96 -8.1; 106 -8.4; 116 -8.6; 128 -8.9; 141 -9.1; 155 -9.3; 170 -9.4; 187 -9.5; 206 -9.5; 227 -9.4; 249 -9.4; 274 -9.4; 302 -9.3; 332 -9.2; 365 -9.1; 402 -9.0; 442 -8.8; 486 -9.0; 535 -9.0; 588 -8.7; 647 -8.9; 712 -9.2; 783 -9.3; 861 -9.8; 947 -10.5; 1042 -11.0; 1146 -11.2; 1261 -11.5; 1387 -11.5; 1526 -11.0; 1678 -9.4; 1846 -8.2; 2031 -6.4; 2234 -4.3; 2457 -3.3; 2703 -2.0; 2973 -0.6; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.6; 5267 -2.5; 5793 -2.1; 6373 -1.1; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NVX EX10S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NVX EX10S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 11 Hz   |  0.25 | 4.7 dB  |
| Peaking | 190 Hz  |  0.41 | -3.1 dB |
| Peaking | 1345 Hz |  1.11 | -6.2 dB |
| Peaking | 3330 Hz |  1.04 | 7.6 dB  |
| Peaking | 6251 Hz |  5.84 | 3.6 dB  |
| Peaking | 2193 Hz | 10.78 | 0.7 dB  |
| Peaking | 3628 Hz |  3.78 | -1.3 dB |
| Peaking | 4284 Hz |  2.33 | 1.3 dB  |
| Peaking | 8493 Hz |  2.28 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.4 dB  |
| Peaking | 62 Hz    | 1.41 | 0.0 dB  |
| Peaking | 125 Hz   | 1.41 | -2.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | -5.1 dB |
| Peaking | 2000 Hz  | 1.41 | -0.8 dB |
| Peaking | 4000 Hz  | 1.41 | 8.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NVX%20EX10S/NVX%20EX10S.png)