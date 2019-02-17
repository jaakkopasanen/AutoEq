# Ultrasone PRO 2900
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.1; 23 -3.2; 25 -4.3; 28 -5.8; 31 -7.0; 34 -7.9; 37 -8.6; 41 -9.3; 45 -9.8; 49 -10.2; 54 -10.5; 60 -10.6; 66 -10.3; 72 -10.1; 79 -10.1; 87 -10.1; 96 -9.9; 106 -9.6; 116 -9.3; 128 -9.0; 141 -8.6; 155 -8.4; 170 -7.7; 187 -7.4; 206 -7.7; 227 -8.7; 249 -8.5; 274 -7.7; 302 -7.0; 332 -6.5; 365 -6.0; 402 -5.7; 442 -5.4; 486 -5.3; 535 -4.9; 588 -3.6; 647 -3.8; 712 -4.3; 783 -4.4; 861 -5.1; 947 -5.7; 1042 -6.3; 1146 -6.6; 1261 -7.1; 1387 -7.0; 1526 -7.4; 1678 -7.8; 1846 -7.7; 2031 -7.6; 2234 -0.5; 2457 -5.8; 2703 -8.0; 2973 -9.0; 3270 -10.6; 3597 -12.2; 3957 -12.1; 4353 -8.8; 4788 -0.5; 5267 -3.4; 5793 -8.9; 6373 -12.4; 7010 -8.4; 7711 -5.9; 8482 -6.1; 9330 -6.1; 10263 -6.1; 11289 -6.1; 12418 -6.1; 13660 -9.2; 15026 -14.8; 16529 -13.5; 18182 -8.9; 20000 -6.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone PRO 2900 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone PRO 2900 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 19 Hz    | 1.39 | 6.2 dB  |
| Peaking | 59 Hz    | 0.5  | -4.8 dB |
| Peaking | 3628 Hz  | 4.44 | -7.0 dB |
| Peaking | 15233 Hz | 3.41 | -7.1 dB |
| Peaking | 16549 Hz | 2.05 | -5.7 dB |
| Peaking | 644 Hz   | 2.08 | 2.9 dB  |
| Peaking | 2109 Hz  | 1.58 | -3.8 dB |
| Peaking | 2235 Hz  | 7.06 | 10.1 dB |
| Peaking | 4919 Hz  | 8.37 | 8.5 dB  |
| Peaking | 6356 Hz  | 6.8  | -6.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.5 dB  |
| Peaking | 62 Hz    | 1.41 | -4.8 dB |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | 2.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.3 dB |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -8.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ultrasone%20PRO%202900/Ultrasone%20PRO%202900.png)