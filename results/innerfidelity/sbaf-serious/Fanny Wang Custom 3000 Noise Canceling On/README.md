# Fanny Wang Custom 3000 Noise Canceling On
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -1.1; 28 -2.4; 31 -2.4; 34 -1.6; 37 -0.8; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.6; 72 -1.0; 79 -1.5; 87 -2.1; 96 -3.0; 106 -3.9; 116 -4.5; 128 -5.4; 141 -6.3; 155 -6.6; 170 -6.7; 187 -7.4; 206 -7.8; 227 -7.8; 249 -8.1; 274 -8.0; 302 -7.9; 332 -7.8; 365 -7.2; 402 -7.2; 442 -6.8; 486 -6.9; 535 -6.5; 588 -5.7; 647 -4.9; 712 -4.1; 783 -3.6; 861 -4.3; 947 -4.7; 1042 -5.6; 1146 -6.5; 1261 -7.8; 1387 -9.0; 1526 -8.9; 1678 -7.7; 1846 -5.5; 2031 -3.2; 2234 -1.3; 2457 -0.9; 2703 -3.7; 2973 -9.0; 3270 -10.8; 3597 -8.4; 3957 -7.3; 4353 -8.3; 4788 -7.4; 5267 -6.0; 5793 -3.6; 6373 -2.6; 7010 -4.0; 7711 -7.1; 8482 -12.5; 9330 -14.6; 10263 -12.8; 11289 -7.7; 12418 -6.5; 13660 -6.5; 15026 -7.2; 16529 -6.6; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fanny Wang Custom 3000 Noise Canceling On GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fanny Wang Custom 3000 Noise Canceling On ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 0.65 | 5.2 dB  |
| Peaking | 63 Hz   | 1.39 | 5.2 dB  |
| Peaking | 2326 Hz | 6.08 | 6.6 dB  |
| Peaking | 6570 Hz | 4.19 | 5.8 dB  |
| Peaking | 9297 Hz | 2.92 | -9.2 dB |
| Peaking | 262 Hz  | 1.26 | -2.0 dB |
| Peaking | 793 Hz  | 2.28 | 3.2 dB  |
| Peaking | 1439 Hz | 3.84 | -3.4 dB |
| Peaking | 2716 Hz | 3.11 | 4.9 dB  |
| Peaking | 3108 Hz | 3.49 | -7.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.9 dB  |
| Peaking | 62 Hz    | 1.41 | 5.8 dB  |
| Peaking | 125 Hz   | 1.41 | 0.6 dB  |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.8 dB |
| Peaking | 8000 Hz  | 1.41 | -2.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fanny%20Wang%20Custom%203000%20Noise%20Canceling%20On/Fanny%20Wang%20Custom%203000%20Noise%20Canceling%20On.png)