# Astrotec Delphinus 5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.2; 23 -2.5; 25 -2.8; 28 -3.2; 31 -3.5; 34 -3.8; 37 -4.0; 41 -4.2; 45 -4.4; 49 -4.7; 54 -5.0; 60 -5.3; 66 -5.6; 72 -6.0; 79 -6.4; 87 -6.8; 96 -7.2; 106 -7.7; 116 -8.0; 128 -8.4; 141 -8.7; 155 -8.9; 170 -9.1; 187 -9.3; 206 -9.4; 227 -9.5; 249 -9.5; 274 -9.5; 302 -9.5; 332 -9.5; 365 -9.5; 402 -9.5; 442 -9.6; 486 -9.6; 535 -9.7; 588 -9.9; 647 -10.2; 712 -10.5; 783 -10.9; 861 -11.5; 947 -12.2; 1042 -12.6; 1146 -12.3; 1261 -11.1; 1387 -9.4; 1526 -7.7; 1678 -6.1; 1846 -4.7; 2031 -4.1; 2234 -4.5; 2457 -5.7; 2703 -5.0; 2973 -2.0; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.4; 7010 -6.1; 7711 -8.0; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Astrotec Delphinus 5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Astrotec Delphinus 5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 12 Hz   | 0.19 | 4.2 dB  |
| Peaking | 221 Hz  | 0.35 | -3.2 dB |
| Peaking | 1068 Hz | 1.32 | -5.7 dB |
| Peaking | 1838 Hz | 3.02 | 2.9 dB  |
| Peaking | 4213 Hz | 1.25 | 7.2 dB  |
| Peaking | 2638 Hz | 5.73 | -3.0 dB |
| Peaking | 3082 Hz | 2.51 | 2.6 dB  |
| Peaking | 4141 Hz | 2.81 | -1.9 dB |
| Peaking | 6340 Hz | 3.05 | 5.2 dB  |
| Peaking | 7221 Hz | 2.91 | -5.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.7 dB  |
| Peaking | 62 Hz    | 1.41 | 0.8 dB  |
| Peaking | 125 Hz   | 1.41 | -1.7 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.6 dB |
| Peaking | 1000 Hz  | 1.41 | -6.3 dB |
| Peaking | 2000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Astrotec%20Delphinus%205/Astrotec%20Delphinus%205.png)