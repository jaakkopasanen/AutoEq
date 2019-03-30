# Kennerton Thror
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.0; 23 -4.3; 25 -4.5; 28 -4.7; 31 -4.7; 34 -4.8; 37 -4.9; 41 -5.3; 45 -5.9; 49 -6.4; 54 -6.8; 60 -7.1; 66 -7.3; 72 -7.3; 79 -7.3; 87 -7.3; 96 -7.4; 106 -7.6; 116 -7.6; 128 -7.6; 141 -7.6; 155 -7.6; 170 -7.7; 187 -7.5; 206 -7.1; 227 -7.0; 249 -7.0; 274 -7.0; 302 -7.0; 332 -6.8; 365 -6.4; 402 -6.4; 442 -6.7; 486 -6.4; 535 -5.8; 588 -5.9; 647 -6.7; 712 -7.2; 783 -7.3; 861 -7.0; 947 -6.8; 1042 -6.2; 1146 -5.3; 1261 -4.5; 1387 -4.0; 1526 -3.3; 1678 -1.8; 1846 -0.5; 2031 -1.0; 2234 -1.9; 2457 -2.6; 2703 -4.5; 2973 -6.5; 3270 -7.4; 3597 -6.9; 3957 -6.0; 4353 -5.7; 4788 -6.9; 5267 -8.4; 5793 -8.5; 6373 -7.2; 7010 -6.1; 7711 -5.5; 8482 -5.8; 9330 -5.8; 10263 -5.8; 11289 -5.8; 12418 -5.8; 13660 -5.8; 15026 -5.8; 16529 -5.8; 18182 -5.8; 20000 -5.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Kennerton Thror GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Kennerton Thror ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.66 | 2.6 dB  |
| Peaking | 84 Hz   | 0.35 | -2.3 dB |
| Peaking | 845 Hz  | 2.36 | -1.7 dB |
| Peaking | 1995 Hz | 1.49 | 7.4 dB  |
| Peaking | 3088 Hz | 0.68 | -2.9 dB |
| Peaking | 169 Hz  | 5.03 | -0.2 dB |
| Peaking | 3253 Hz | 5.69 | -1.5 dB |
| Peaking | 4335 Hz | 2.72 | 2.3 dB  |
| Peaking | 5580 Hz | 2.53 | -3.3 dB |
| Peaking | 7081 Hz | 1.64 | 1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.8 dB  |
| Peaking | 62 Hz    | 1.41 | -1.4 dB |
| Peaking | 125 Hz   | 1.41 | -1.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.0 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | -1.6 dB |
| Peaking | 2000 Hz  | 1.41 | 5.6 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.6 dB |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Kennerton%20Thror/Kennerton%20Thror.png)