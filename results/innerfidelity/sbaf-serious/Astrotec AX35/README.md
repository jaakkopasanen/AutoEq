# Astrotec AX35
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.6; 45 -1.2; 49 -1.9; 54 -2.6; 60 -3.5; 66 -4.4; 72 -5.1; 79 -5.8; 87 -6.7; 96 -7.5; 106 -8.2; 116 -8.7; 128 -9.2; 141 -9.7; 155 -10.2; 170 -10.4; 187 -10.6; 206 -10.8; 227 -10.8; 249 -10.8; 274 -10.7; 302 -10.5; 332 -10.3; 365 -10.0; 402 -9.7; 442 -9.2; 486 -8.9; 535 -8.4; 588 -7.6; 647 -7.2; 712 -6.9; 783 -6.3; 861 -6.2; 947 -6.2; 1042 -6.3; 1146 -6.6; 1261 -7.2; 1387 -8.1; 1526 -8.9; 1678 -9.2; 1846 -8.8; 2031 -8.2; 2234 -7.5; 2457 -6.1; 2703 -5.0; 2973 -2.4; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.0; 4788 -1.7; 5267 -1.7; 5793 -3.4; 6373 -6.5; 7010 -4.6; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Astrotec AX35 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Astrotec AX35 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.43 | 7.9 dB  |
| Peaking | 175 Hz  | 0.33 | -5.7 dB |
| Peaking | 943 Hz  | 0.85 | 3.3 dB  |
| Peaking | 1784 Hz | 1.02 | -5.0 dB |
| Peaking | 3701 Hz | 1.31 | 7.8 dB  |
| Peaking | 3153 Hz | 9.94 | 1.4 dB  |
| Peaking | 5289 Hz | 4.38 | 3.3 dB  |
| Peaking | 5709 Hz | 1.34 | -1.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.4 dB  |
| Peaking | 62 Hz    | 1.41 | 2.1 dB  |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | -4.3 dB |
| Peaking | 500 Hz   | 1.41 | -1.5 dB |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.6 dB |
| Peaking | 4000 Hz  | 1.41 | 7.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Astrotec%20AX35/Astrotec%20AX35.png)