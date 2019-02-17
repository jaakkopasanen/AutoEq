# Klipsch X12i
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.4; 23 -7.5; 25 -7.6; 28 -7.8; 31 -7.9; 34 -8.0; 37 -8.2; 41 -8.3; 45 -8.5; 49 -8.7; 54 -8.9; 60 -9.2; 66 -9.5; 72 -9.8; 79 -10.1; 87 -10.5; 96 -10.9; 106 -11.1; 116 -11.2; 128 -11.5; 141 -11.6; 155 -11.7; 170 -11.8; 187 -11.7; 206 -11.7; 227 -11.4; 249 -11.3; 274 -11.1; 302 -10.8; 332 -10.5; 365 -10.1; 402 -9.7; 442 -9.2; 486 -8.9; 535 -8.4; 588 -7.7; 647 -7.3; 712 -7.0; 783 -6.4; 861 -6.3; 947 -6.4; 1042 -6.6; 1146 -6.7; 1261 -6.7; 1387 -7.1; 1526 -7.3; 1678 -7.3; 1846 -6.8; 2031 -6.3; 2234 -6.0; 2457 -5.6; 2703 -5.7; 2973 -5.7; 3270 -4.7; 3597 -2.1; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Klipsch X12i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch X12i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 128 Hz  | 0.49 | -4.5 dB |
| Peaking | 286 Hz  | 1    | -2.1 dB |
| Peaking | 3072 Hz | 4.96 | -1.3 dB |
| Peaking | 4149 Hz | 2.17 | 6.0 dB  |
| Peaking | 5884 Hz | 3.38 | 4.9 dB  |
| Peaking | 26 Hz   | 1.44 | -0.4 dB |
| Peaking | 837 Hz  | 3.24 | 0.9 dB  |
| Peaking | 1599 Hz | 3.95 | -1.1 dB |
| Peaking | 8229 Hz | 4.45 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.0 dB |
| Peaking | 62 Hz    | 1.41 | -2.0 dB |
| Peaking | 125 Hz   | 1.41 | -4.3 dB |
| Peaking | 250 Hz   | 1.41 | -4.3 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Klipsch%20X12i/Klipsch%20X12i.png)