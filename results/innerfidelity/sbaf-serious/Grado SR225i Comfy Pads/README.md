# Grado SR225i Comfy Pads
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.8; 37 -1.5; 41 -2.6; 45 -3.5; 49 -4.2; 54 -5.1; 60 -5.7; 66 -6.3; 72 -6.9; 79 -7.3; 87 -7.8; 96 -8.2; 106 -8.4; 116 -8.4; 128 -8.5; 141 -8.5; 155 -8.4; 170 -8.3; 187 -8.2; 206 -8.0; 227 -7.7; 249 -7.5; 274 -7.2; 302 -7.3; 332 -7.2; 365 -6.9; 402 -6.8; 442 -6.6; 486 -6.6; 535 -6.5; 588 -6.2; 647 -6.1; 712 -6.2; 783 -6.0; 861 -6.2; 947 -6.4; 1042 -6.5; 1146 -6.7; 1261 -7.1; 1387 -8.0; 1526 -9.3; 1678 -10.1; 1846 -11.3; 2031 -15.3; 2234 -15.8; 2457 -12.4; 2703 -10.0; 2973 -8.2; 3270 -6.7; 3597 -7.8; 3957 -6.3; 4353 -4.4; 4788 -4.8; 5267 -6.2; 5793 -3.5; 6373 -3.7; 7010 -6.5; 7711 -7.8; 8482 -8.9; 9330 -9.0; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR225i Comfy Pads GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR225i Comfy Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 27 Hz   | 0.77 | 6.7 dB   |
| Peaking | 111 Hz  | 0.71 | -2.8 dB  |
| Peaking | 2157 Hz | 2.9  | -10.1 dB |
| Peaking | 6495 Hz | 1.13 | 4.0 dB   |
| Peaking | 8276 Hz | 2.23 | -5.3 dB  |
| Peaking | 826 Hz  | 1.21 | 0.7 dB   |
| Peaking | 1526 Hz | 7.37 | -1.0 dB  |
| Peaking | 4536 Hz | 5.63 | 3.3 dB   |
| Peaking | 5191 Hz | 2.39 | -3.1 dB  |
| Peaking | 5969 Hz | 5.88 | 3.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.2 dB  |
| Peaking | 62 Hz    | 1.41 | -0.6 dB |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -8.3 dB |
| Peaking | 4000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20SR225i%20Comfy%20Pads/Grado%20SR225i%20Comfy%20Pads.png)