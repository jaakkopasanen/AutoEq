# Meze 99 Classics
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.6; 23 -14.6; 25 -14.6; 28 -14.7; 31 -14.8; 34 -14.9; 37 -15.0; 41 -14.9; 45 -14.8; 49 -14.8; 54 -14.9; 60 -15.0; 66 -14.8; 72 -14.5; 79 -14.3; 87 -14.4; 96 -14.6; 106 -14.6; 116 -14.7; 128 -14.5; 141 -14.1; 155 -13.5; 170 -12.7; 187 -11.8; 206 -10.4; 227 -8.5; 249 -6.8; 274 -5.0; 302 -3.3; 332 -1.7; 365 -0.5; 402 -0.5; 442 -1.2; 486 -2.5; 535 -3.6; 588 -4.4; 647 -5.0; 712 -5.2; 783 -5.2; 861 -5.2; 947 -5.2; 1042 -5.0; 1146 -5.2; 1261 -5.5; 1387 -5.9; 1526 -6.3; 1678 -6.6; 1846 -6.9; 2031 -6.9; 2234 -7.1; 2457 -7.5; 2703 -7.8; 2973 -7.8; 3270 -6.9; 3597 -5.6; 3957 -6.1; 4353 -7.9; 4788 -8.8; 5267 -8.7; 5793 -8.0; 6373 -7.0; 7010 -5.1; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Meze 99 Classics GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Meze 99 Classics ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 84 Hz   |  0.12 | -9.2 dB |
| Peaking | 362 Hz  |  1.24 | 11.4 dB |
| Peaking | 735 Hz  |  0.47 | 3.2 dB  |
| Peaking | 2439 Hz |  2.14 | -1.6 dB |
| Peaking | 5055 Hz |  4.54 | -2.8 dB |
| Peaking | 149 Hz  |  2.74 | -0.8 dB |
| Peaking | 250 Hz  |  5.42 | 0.9 dB  |
| Peaking | 3715 Hz | 10.18 | 1.6 dB  |
| Peaking | 7090 Hz |  9.66 | 1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.6 dB |
| Peaking | 62 Hz    | 1.41 | -5.5 dB |
| Peaking | 125 Hz   | 1.41 | -8.5 dB |
| Peaking | 250 Hz   | 1.41 | 1.3 dB  |
| Peaking | 500 Hz   | 1.41 | 5.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.4 dB |
| Peaking | 4000 Hz  | 1.41 | -1.0 dB |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Meze%2099%20Classics/Meze%2099%20Classics.png)