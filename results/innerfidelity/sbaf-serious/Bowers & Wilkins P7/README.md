# Bowers & Wilkins P7
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.0; 23 -5.4; 25 -5.7; 28 -6.1; 31 -6.4; 34 -6.7; 37 -6.9; 41 -7.0; 45 -7.1; 49 -7.3; 54 -7.1; 60 -7.2; 66 -7.8; 72 -8.1; 79 -8.2; 87 -8.1; 96 -7.7; 106 -6.8; 116 -6.3; 128 -6.9; 141 -7.7; 155 -7.7; 170 -6.5; 187 -7.1; 206 -6.5; 227 -5.9; 249 -5.2; 274 -4.5; 302 -4.0; 332 -3.8; 365 -3.6; 402 -3.7; 442 -3.5; 486 -3.6; 535 -3.7; 588 -3.5; 647 -3.7; 712 -4.4; 783 -5.1; 861 -5.7; 947 -5.5; 1042 -5.9; 1146 -6.4; 1261 -7.2; 1387 -8.4; 1526 -9.3; 1678 -10.0; 1846 -10.0; 2031 -9.6; 2234 -8.9; 2457 -7.0; 2703 -3.7; 2973 -1.7; 3270 -1.9; 3597 -4.1; 3957 -5.6; 4353 -5.5; 4788 -4.5; 5267 -3.1; 5793 -3.9; 6373 -0.5; 7010 -3.2; 7711 -5.4; 8482 -5.7; 9330 -5.7; 10263 -5.7; 11289 -5.7; 12418 -5.7; 13660 -5.7; 15026 -5.7; 16529 -5.7; 18182 -5.7; 20000 -5.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bowers & Wilkins P7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bowers & Wilkins P7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 144 Hz  | 0.32 | -2.6 dB |
| Peaking | 412 Hz  | 0.64 | 4.1 dB  |
| Peaking | 1883 Hz | 1.28 | -5.5 dB |
| Peaking | 3014 Hz | 3.14 | 6.4 dB  |
| Peaking | 6403 Hz | 4.57 | 5.0 dB  |
| Peaking | 15 Hz   | 1.75 | 1.5 dB  |
| Peaking | 109 Hz  | 1.39 | -1.7 dB |
| Peaking | 113 Hz  | 3.48 | 3.0 dB  |
| Peaking | 5132 Hz | 5.84 | 3.2 dB  |
| Peaking | 5185 Hz | 2.08 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.2 dB |
| Peaking | 62 Hz    | 1.41 | -2.0 dB |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | 0.3 dB  |
| Peaking | 500 Hz   | 1.41 | 2.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | -4.2 dB |
| Peaking | 4000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bowers%20&%20Wilkins%20P7/Bowers%20&%20Wilkins%20P7.png)