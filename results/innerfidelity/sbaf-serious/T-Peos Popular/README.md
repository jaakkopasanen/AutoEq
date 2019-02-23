# T-Peos Popular
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.3; 23 -13.2; 25 -13.2; 28 -13.1; 31 -13.0; 34 -12.8; 37 -12.7; 41 -12.5; 45 -12.3; 49 -12.1; 54 -12.0; 60 -11.8; 66 -11.7; 72 -11.6; 79 -11.5; 87 -11.4; 96 -11.2; 106 -11.0; 116 -10.6; 128 -10.5; 141 -10.2; 155 -9.8; 170 -9.4; 187 -9.0; 206 -8.5; 227 -8.0; 249 -7.6; 274 -7.1; 302 -6.6; 332 -6.1; 365 -5.6; 402 -5.1; 442 -4.6; 486 -4.4; 535 -4.0; 588 -3.5; 647 -3.4; 712 -3.4; 783 -3.3; 861 -3.7; 947 -4.3; 1042 -5.5; 1146 -4.9; 1261 -6.2; 1387 -7.5; 1526 -9.0; 1678 -10.4; 1846 -11.4; 2031 -12.0; 2234 -11.7; 2457 -9.2; 2703 -6.0; 2973 -2.5; 3270 -0.6; 3597 -0.5; 3957 -1.0; 4353 -4.4; 4788 -8.0; 5267 -11.2; 5793 -8.4; 6373 -4.2; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -7.7; 10263 -7.2; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`T-Peos Popular GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `T-Peos Popular ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.5dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 22 Hz   | 0.26 | -6.6 dB  |
| Peaking | 128 Hz  | 0.96 | -2.3 dB  |
| Peaking | 1929 Hz | 1.4  | -16.6 dB |
| Peaking | 2181 Hz | 0.41 | 10.3 dB  |
| Peaking | 5305 Hz | 4.92 | -9.5 dB  |
| Peaking | 645 Hz  | 1.26 | 1.2 dB   |
| Peaking | 1103 Hz | 2.14 | -1.4 dB  |
| Peaking | 2415 Hz | 6.12 | -3.1 dB  |
| Peaking | 3406 Hz | 3.45 | 3.3 dB   |
| Peaking | 9511 Hz | 2.44 | -2.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.9 dB |
| Peaking | 62 Hz    | 1.41 | -3.8 dB |
| Peaking | 125 Hz   | 1.41 | -3.5 dB |
| Peaking | 250 Hz   | 1.41 | -1.0 dB |
| Peaking | 500 Hz   | 1.41 | 2.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.1 dB |
| Peaking | 4000 Hz  | 1.41 | 5.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/T-Peos%20Popular/T-Peos%20Popular.png)