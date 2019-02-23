# Aiaiai TMA-1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.7; 23 -1.2; 25 -1.9; 28 -3.1; 31 -4.3; 34 -5.3; 37 -6.2; 41 -7.2; 45 -7.9; 49 -8.6; 54 -9.3; 60 -9.8; 66 -10.2; 72 -10.4; 79 -10.9; 87 -11.1; 96 -11.1; 106 -11.3; 116 -11.9; 128 -12.2; 141 -12.4; 155 -12.5; 170 -12.3; 187 -12.6; 206 -12.7; 227 -12.6; 249 -12.6; 274 -12.3; 302 -12.6; 332 -12.9; 365 -12.9; 402 -12.3; 442 -11.8; 486 -11.5; 535 -10.5; 588 -9.0; 647 -7.3; 712 -6.1; 783 -5.9; 861 -7.3; 947 -8.4; 1042 -8.4; 1146 -7.7; 1261 -6.7; 1387 -6.4; 1526 -5.6; 1678 -4.5; 1846 -3.1; 2031 -1.6; 2234 -0.6; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -3.6; 5267 -4.0; 5793 -3.3; 6373 -6.6; 7010 -5.3; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Aiaiai TMA-1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Aiaiai TMA-1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.78 | 7.1 dB  |
| Peaking | 53 Hz   | 0.69 | -2.8 dB |
| Peaking | 190 Hz  | 0.48 | -5.6 dB |
| Peaking | 395 Hz  | 1.89 | -2.8 dB |
| Peaking | 3040 Hz | 1.05 | 7.0 dB  |
| Peaking | 741 Hz  | 3.6  | 3.2 dB  |
| Peaking | 991 Hz  | 3.38 | -1.6 dB |
| Peaking | 2114 Hz | 2.76 | 3.0 dB  |
| Peaking | 2456 Hz | 0.33 | -1.5 dB |
| Peaking | 4269 Hz | 4.05 | 2.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.8 dB  |
| Peaking | 62 Hz    | 1.41 | -3.7 dB |
| Peaking | 125 Hz   | 1.41 | -4.2 dB |
| Peaking | 250 Hz   | 1.41 | -5.7 dB |
| Peaking | 500 Hz   | 1.41 | -3.0 dB |
| Peaking | 1000 Hz  | 1.41 | -1.3 dB |
| Peaking | 2000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Aiaiai%20TMA-1/Aiaiai%20TMA-1.png)