# Astell & Kern AKR03 Roxanne (min)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.2; 23 -6.5; 25 -6.8; 28 -7.2; 31 -7.5; 34 -7.8; 37 -8.1; 41 -8.4; 45 -8.7; 49 -9.0; 54 -9.2; 60 -9.5; 66 -9.6; 72 -9.8; 79 -9.9; 87 -10.1; 96 -10.2; 106 -10.2; 116 -10.4; 128 -10.5; 141 -10.5; 155 -10.5; 170 -10.5; 187 -10.5; 206 -10.5; 227 -10.5; 249 -10.5; 274 -10.5; 302 -10.5; 332 -10.5; 365 -10.2; 402 -10.1; 442 -9.9; 486 -9.6; 535 -9.2; 588 -8.9; 647 -8.5; 712 -8.0; 783 -7.6; 861 -7.1; 947 -6.6; 1042 -6.2; 1146 -5.9; 1261 -5.6; 1387 -5.2; 1526 -4.4; 1678 -3.4; 1846 -2.2; 2031 -1.1; 2234 -0.5; 2457 -0.5; 2703 -1.5; 2973 -3.0; 3270 -3.4; 3597 -2.0; 3957 -1.0; 4353 -2.3; 4788 -3.4; 5267 -3.5; 5793 -3.6; 6373 -2.8; 7010 -3.3; 7711 -5.4; 8482 -5.7; 9330 -5.7; 10263 -5.7; 11289 -5.7; 12418 -5.7; 13660 -5.7; 15026 -5.7; 16529 -5.7; 18182 -5.7; 20000 -5.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Astell & Kern AKR03 Roxanne (min) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Astell & Kern AKR03 Roxanne (min) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 100 Hz   | 0.39 | -4.1 dB |
| Peaking | 391 Hz   | 0.63 | -3.3 dB |
| Peaking | 2185 Hz  | 1.97 | 4.9 dB  |
| Peaking | 4329 Hz  | 1.19 | 3.1 dB  |
| Peaking | 22050 Hz | 2.23 | 0.7 dB  |
| Peaking | 17 Hz    | 1.5  | 0.7 dB  |
| Peaking | 3236 Hz  | 7.39 | -1.1 dB |
| Peaking | 3872 Hz  | 6.36 | 1.8 dB  |
| Peaking | 6631 Hz  | 3.98 | 4.2 dB  |
| Peaking | 6632 Hz  | 1.47 | -2.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.3 dB |
| Peaking | 62 Hz    | 1.41 | -3.2 dB |
| Peaking | 125 Hz   | 1.41 | -3.7 dB |
| Peaking | 250 Hz   | 1.41 | -4.0 dB |
| Peaking | 500 Hz   | 1.41 | -3.3 dB |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB |
| Peaking | 2000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Astell%20&%20Kern%20AKR03%20Roxanne%20(min)/Astell%20&%20Kern%20AKR03%20Roxanne%20(min).png)