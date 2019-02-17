# Aiaiai TMA-1 Studio
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.6; 28 -1.3; 31 -2.4; 34 -3.4; 37 -4.3; 41 -5.4; 45 -6.2; 49 -6.9; 54 -7.5; 60 -8.0; 66 -8.4; 72 -8.7; 79 -9.0; 87 -9.1; 96 -9.3; 106 -9.1; 116 -9.1; 128 -9.3; 141 -9.7; 155 -9.9; 170 -9.6; 187 -9.5; 206 -9.5; 227 -9.4; 249 -9.3; 274 -9.0; 302 -8.4; 332 -8.1; 365 -8.4; 402 -8.1; 442 -7.9; 486 -7.8; 535 -7.3; 588 -6.3; 647 -5.5; 712 -4.9; 783 -4.7; 861 -5.3; 947 -6.2; 1042 -6.6; 1146 -6.4; 1261 -5.3; 1387 -5.2; 1526 -4.8; 1678 -4.0; 1846 -2.9; 2031 -1.8; 2234 -0.8; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -1.2; 3957 -1.3; 4353 -0.6; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.1; 7010 -5.2; 7711 -6.3; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Aiaiai TMA-1 Studio GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Aiaiai TMA-1 Studio ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 0.9  | 8.1 dB  |
| Peaking | 99 Hz   | 0.23 | -3.5 dB |
| Peaking | 717 Hz  | 3.3  | 2.5 dB  |
| Peaking | 2692 Hz | 1.17 | 6.2 dB  |
| Peaking | 5313 Hz | 2.29 | 5.2 dB  |
| Peaking | 1079 Hz | 6.67 | -1.0 dB |
| Peaking | 2081 Hz | 6.19 | 0.6 dB  |
| Peaking | 6375 Hz | 7.18 | 2.1 dB  |
| Peaking | 6382 Hz | 5.67 | 1.0 dB  |
| Peaking | 7387 Hz | 2.14 | -2.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.5 dB  |
| Peaking | 62 Hz    | 1.41 | -2.7 dB |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Aiaiai%20TMA-1%20Studio/Aiaiai%20TMA-1%20Studio.png)