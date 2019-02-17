# Astrotec AX7
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.6; 49 -0.9; 54 -1.2; 60 -1.5; 66 -1.9; 72 -2.4; 79 -2.9; 87 -3.4; 96 -4.0; 106 -4.3; 116 -4.7; 128 -5.1; 141 -5.6; 155 -5.9; 170 -6.1; 187 -6.4; 206 -6.7; 227 -6.7; 249 -6.9; 274 -6.9; 302 -7.0; 332 -7.0; 365 -6.9; 402 -6.8; 442 -6.6; 486 -6.6; 535 -6.4; 588 -6.0; 647 -5.9; 712 -5.9; 783 -5.7; 861 -5.9; 947 -6.2; 1042 -6.6; 1146 -6.8; 1261 -7.3; 1387 -7.7; 1526 -8.2; 1678 -8.4; 1846 -8.3; 2031 -8.1; 2234 -7.7; 2457 -6.3; 2703 -3.9; 2973 -0.7; 3270 -0.5; 3597 -0.5; 3957 -0.6; 4353 -4.6; 4788 -5.0; 5267 -3.1; 5793 -2.0; 6373 -1.5; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Astrotec AX7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Astrotec AX7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 34 Hz   |  0.55 | 6.6 dB  |
| Peaking | 841 Hz  |  2.1  | 1.3 dB  |
| Peaking | 2187 Hz |  0.89 | -3.9 dB |
| Peaking | 3264 Hz |  1.9  | 9.0 dB  |
| Peaking | 6167 Hz |  4.17 | 4.9 dB  |
| Peaking | 34 Hz   |  2.66 | -0.7 dB |
| Peaking | 71 Hz   |  1.14 | 0.6 dB  |
| Peaking | 234 Hz  |  1.15 | -0.9 dB |
| Peaking | 3909 Hz | 16.39 | 1.8 dB  |
| Peaking | 8216 Hz |  4.4  | -0.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.7 dB  |
| Peaking | 62 Hz    | 1.41 | 3.8 dB  |
| Peaking | 125 Hz   | 1.41 | 0.7 dB  |
| Peaking | 250 Hz   | 1.41 | -1.0 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.6 dB |
| Peaking | 4000 Hz  | 1.41 | 6.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Astrotec%20AX7/Astrotec%20AX7.png)