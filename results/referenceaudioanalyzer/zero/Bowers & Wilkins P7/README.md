# Bowers & Wilkins P7
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.0; 23 -12.2; 25 -12.4; 28 -12.6; 31 -12.7; 34 -12.8; 37 -12.9; 41 -12.9; 45 -12.9; 49 -12.8; 54 -12.6; 60 -12.5; 66 -12.3; 72 -11.9; 79 -11.6; 87 -11.3; 96 -11.0; 106 -10.8; 116 -10.6; 128 -10.4; 141 -10.3; 155 -10.0; 170 -9.7; 187 -9.1; 206 -8.1; 227 -7.0; 249 -6.0; 274 -4.9; 302 -4.0; 332 -3.4; 365 -3.1; 402 -3.4; 442 -3.7; 486 -3.9; 535 -4.3; 588 -4.7; 647 -5.1; 712 -5.6; 783 -6.1; 861 -6.4; 947 -6.4; 1042 -6.4; 1146 -6.7; 1261 -6.5; 1387 -6.4; 1526 -6.4; 1678 -6.5; 1846 -6.7; 2031 -6.4; 2234 -5.2; 2457 -3.1; 2703 -0.9; 2973 -0.5; 3270 -2.1; 3597 -4.1; 3957 -4.8; 4353 -4.6; 4788 -4.1; 5267 -4.1; 5793 -4.4; 6373 -4.4; 7010 -3.5; 7711 -4.8; 8482 -5.1; 9330 -5.1; 10263 -5.1; 11289 -5.1; 12418 -5.1; 13660 -5.1; 15026 -5.1; 16529 -5.1; 18182 -5.1; 20000 -5.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bowers & Wilkins P7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bowers & Wilkins P7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.62 | -2.4 dB |
| Peaking | 109 Hz  | 0.13 | -6.6 dB |
| Peaking | 369 Hz  | 0.85 | 7.7 dB  |
| Peaking | 2039 Hz | 1.89 | -2.2 dB |
| Peaking | 2819 Hz | 2.63 | 6.0 dB  |
| Peaking | 169 Hz  | 1.24 | 1.0 dB  |
| Peaking | 171 Hz  | 2.3  | -1.7 dB |
| Peaking | 617 Hz  | 5.89 | 0.5 dB  |
| Peaking | 3855 Hz | 5.71 | -1.1 dB |
| Peaking | 5937 Hz | 1.55 | 0.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.0 dB |
| Peaking | 62 Hz    | 1.41 | -5.3 dB |
| Peaking | 125 Hz   | 1.41 | -5.0 dB |
| Peaking | 250 Hz   | 1.41 | 0.0 dB  |
| Peaking | 500 Hz   | 1.41 | 2.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.4 dB |
| Peaking | 2000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Bowers%20&%20Wilkins%20P7/Bowers%20&%20Wilkins%20P7.png)