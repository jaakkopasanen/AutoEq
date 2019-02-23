# Ultrasone PRO 2900
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.0; 23 -3.1; 25 -4.2; 28 -5.7; 31 -6.9; 34 -7.8; 37 -8.5; 41 -9.2; 45 -9.7; 49 -10.1; 54 -10.4; 60 -10.5; 66 -10.3; 72 -10.0; 79 -10.1; 87 -10.0; 96 -9.8; 106 -9.5; 116 -9.2; 128 -8.9; 141 -8.6; 155 -8.3; 170 -7.7; 187 -7.3; 206 -7.7; 227 -8.6; 249 -8.4; 274 -7.6; 302 -6.9; 332 -6.4; 365 -5.9; 402 -5.6; 442 -5.3; 486 -5.2; 535 -4.9; 588 -3.5; 647 -3.7; 712 -4.3; 783 -4.4; 861 -5.0; 947 -5.7; 1042 -6.3; 1146 -6.6; 1261 -7.0; 1387 -6.9; 1526 -7.3; 1678 -7.7; 1846 -7.6; 2031 -7.5; 2234 -0.5; 2457 -5.7; 2703 -7.9; 2973 -8.9; 3270 -10.5; 3597 -12.1; 3957 -12.0; 4353 -8.7; 4788 -0.8; 5267 -3.4; 5793 -8.9; 6373 -12.3; 7010 -8.3; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -9.2; 15026 -14.7; 16529 -13.4; 18182 -8.8; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone PRO 2900 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone PRO 2900 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 1.62 | 6.0 dB  |
| Peaking | 62 Hz    | 0.64 | -4.3 dB |
| Peaking | 3642 Hz  | 5.05 | -6.6 dB |
| Peaking | 15013 Hz | 3.66 | -6.7 dB |
| Peaking | 16688 Hz | 2.26 | -5.7 dB |
| Peaking | 649 Hz   | 1.76 | 3.2 dB  |
| Peaking | 2157 Hz  | 1.54 | -3.5 dB |
| Peaking | 2246 Hz  | 6.95 | 10.1 dB |
| Peaking | 4914 Hz  | 8.02 | 8.3 dB  |
| Peaking | 6347 Hz  | 7.02 | -6.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.9 dB  |
| Peaking | 62 Hz    | 1.41 | -4.5 dB |
| Peaking | 125 Hz   | 1.41 | -1.5 dB |
| Peaking | 250 Hz   | 1.41 | -1.5 dB |
| Peaking | 500 Hz   | 1.41 | 2.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.8 dB |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -7.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ultrasone%20PRO%202900/Ultrasone%20PRO%202900.png)