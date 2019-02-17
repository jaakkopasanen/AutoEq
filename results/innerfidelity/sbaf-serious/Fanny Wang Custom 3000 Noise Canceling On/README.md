# Fanny Wang Custom 3000 Noise Canceling On
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.8; 25 -2.0; 28 -3.6; 31 -3.7; 34 -2.9; 37 -2.0; 41 -1.4; 45 -1.1; 49 -1.0; 54 -1.1; 60 -1.5; 66 -1.9; 72 -2.3; 79 -2.8; 87 -3.4; 96 -4.3; 106 -5.2; 116 -5.8; 128 -6.7; 141 -7.5; 155 -7.8; 170 -8.0; 187 -8.7; 206 -9.1; 227 -9.1; 249 -9.4; 274 -9.3; 302 -9.2; 332 -9.1; 365 -8.5; 402 -8.5; 442 -8.1; 486 -8.2; 535 -7.8; 588 -7.0; 647 -6.2; 712 -5.3; 783 -4.8; 861 -5.6; 947 -6.0; 1042 -6.8; 1146 -7.8; 1261 -9.1; 1387 -10.2; 1526 -10.2; 1678 -9.0; 1846 -6.8; 2031 -4.5; 2234 -2.6; 2457 -2.2; 2703 -5.0; 2973 -10.3; 3270 -12.1; 3597 -9.7; 3957 -8.6; 4353 -9.6; 4788 -8.7; 5267 -7.3; 5793 -4.9; 6373 -3.9; 7010 -4.5; 7711 -8.3; 8482 -13.7; 9330 -15.9; 10263 -14.1; 11289 -8.8; 12418 -6.5; 13660 -6.5; 15026 -8.5; 16529 -7.3; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fanny Wang Custom 3000 Noise Canceling On GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fanny Wang Custom 3000 Noise Canceling On ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 20 Hz   | 1.4  | 5.8 dB   |
| Peaking | 55 Hz   | 1.55 | 5.6 dB   |
| Peaking | 2343 Hz | 3.15 | 13.3 dB  |
| Peaking | 2460 Hz | 1.04 | -7.8 dB  |
| Peaking | 9479 Hz | 4.11 | -10.5 dB |
| Peaking | 271 Hz  | 1    | -3.1 dB  |
| Peaking | 803 Hz  | 2.49 | 2.7 dB   |
| Peaking | 1405 Hz | 5.42 | -2.4 dB  |
| Peaking | 6479 Hz | 2.59 | 8.3 dB   |
| Peaking | 6784 Hz | 1.06 | -3.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.8 dB  |
| Peaking | 62 Hz    | 1.41 | 5.2 dB  |
| Peaking | 125 Hz   | 1.41 | -0.4 dB |
| Peaking | 250 Hz   | 1.41 | -3.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB |
| Peaking | 2000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.8 dB |
| Peaking | 8000 Hz  | 1.41 | -3.5 dB |
| Peaking | 16000 Hz | 1.41 | -1.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fanny%20Wang%20Custom%203000%20Noise%20Canceling%20On/Fanny%20Wang%20Custom%203000%20Noise%20Canceling%20On.png)