# Aiaiai TMA-1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.6; 28 -1.2; 31 -2.2; 34 -3.2; 37 -4.1; 41 -5.1; 45 -5.9; 49 -6.5; 54 -7.2; 60 -7.7; 66 -8.1; 72 -8.3; 79 -8.8; 87 -9.0; 96 -9.0; 106 -9.2; 116 -9.8; 128 -10.1; 141 -10.3; 155 -10.4; 170 -10.2; 187 -10.5; 206 -10.7; 227 -10.5; 249 -10.5; 274 -10.2; 302 -10.5; 332 -10.8; 365 -10.8; 402 -10.3; 442 -9.8; 486 -9.5; 535 -8.5; 588 -6.9; 647 -5.2; 712 -4.0; 783 -3.9; 861 -5.2; 947 -6.4; 1042 -6.3; 1146 -5.6; 1261 -4.7; 1387 -4.4; 1526 -3.6; 1678 -2.5; 1846 -1.0; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.7; 5267 -1.9; 5793 -1.2; 6373 -4.6; 7010 -4.4; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Aiaiai TMA-1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Aiaiai TMA-1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 24 Hz   |  1.35 | 6.6 dB  |
| Peaking | 150 Hz  |  0.59 | -3.9 dB |
| Peaking | 365 Hz  |  2.04 | -3.1 dB |
| Peaking | 2336 Hz |  0.92 | 5.7 dB  |
| Peaking | 4538 Hz |  1.62 | 3.9 dB  |
| Peaking | 510 Hz  |  4.2  | -1.6 dB |
| Peaking | 752 Hz  |  2.45 | 3.8 dB  |
| Peaking | 970 Hz  |  2.34 | -2.4 dB |
| Peaking | 5757 Hz | 10.54 | 2.5 dB  |
| Peaking | 8449 Hz |  1.5  | -0.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.7 dB  |
| Peaking | 62 Hz    | 1.41 | -2.2 dB |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | -4.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.5 dB |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Aiaiai%20TMA-1/Aiaiai%20TMA-1.png)