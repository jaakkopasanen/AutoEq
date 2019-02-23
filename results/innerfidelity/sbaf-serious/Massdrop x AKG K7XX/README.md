# Massdrop x AKG K7XX
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.4; 23 -3.8; 25 -4.3; 28 -4.8; 31 -5.2; 34 -5.6; 37 -5.8; 41 -6.1; 45 -6.4; 49 -6.6; 54 -6.9; 60 -7.2; 66 -7.5; 72 -7.7; 79 -8.0; 87 -8.4; 96 -8.8; 106 -8.9; 116 -9.1; 128 -9.2; 141 -9.3; 155 -9.4; 170 -9.4; 187 -9.0; 206 -9.0; 227 -9.1; 249 -9.0; 274 -9.0; 302 -8.9; 332 -8.6; 365 -8.3; 402 -8.0; 442 -7.4; 486 -7.1; 535 -6.6; 588 -5.8; 647 -5.2; 712 -4.5; 783 -3.8; 861 -3.4; 947 -3.8; 1042 -4.0; 1146 -4.6; 1261 -5.1; 1387 -6.1; 1526 -7.6; 1678 -9.1; 1846 -9.5; 2031 -9.6; 2234 -8.4; 2457 -5.4; 2703 -2.6; 2973 -0.5; 3270 -0.5; 3597 -2.2; 3957 -4.0; 4353 -5.3; 4788 -4.7; 5267 -2.6; 5793 -2.5; 6373 -3.9; 7010 -6.6; 7711 -7.1; 8482 -8.6; 9330 -7.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -7.9; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop x AKG K7XX GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x AKG K7XX ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 2.8  | 3.4 dB  |
| Peaking | 936 Hz   | 2.29 | 3.5 dB  |
| Peaking | 1978 Hz  | 2.27 | -4.9 dB |
| Peaking | 3065 Hz  | 2.59 | 7.3 dB  |
| Peaking | 5596 Hz  | 5.36 | 4.3 dB  |
| Peaking | 28 Hz    | 0.93 | 0.8 dB  |
| Peaking | 134 Hz   | 0.78 | -2.9 dB |
| Peaking | 299 Hz   | 1.82 | -1.7 dB |
| Peaking | 8648 Hz  | 5.32 | -2.7 dB |
| Peaking | 18479 Hz | 3.17 | -1.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.0 dB  |
| Peaking | 62 Hz    | 1.41 | -0.9 dB |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.5 dB |
| Peaking | 4000 Hz  | 1.41 | 5.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Massdrop%20x%20AKG%20K7XX/Massdrop%20x%20AKG%20K7XX.png)