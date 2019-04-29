# Soranic SP3 SE
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.4; 23 -4.7; 25 -4.9; 28 -5.1; 31 -5.2; 34 -5.3; 37 -5.4; 41 -5.5; 45 -5.6; 49 -5.7; 54 -5.8; 60 -5.9; 66 -6.0; 72 -6.1; 79 -6.2; 87 -6.4; 96 -6.5; 106 -6.6; 116 -6.7; 128 -6.7; 141 -6.6; 155 -6.5; 170 -6.4; 187 -6.2; 206 -6.0; 227 -5.8; 249 -5.5; 274 -5.3; 302 -5.0; 332 -4.8; 365 -4.6; 402 -4.4; 442 -4.2; 486 -4.0; 535 -3.8; 588 -3.7; 647 -3.5; 712 -3.2; 783 -3.1; 861 -3.0; 947 -3.1; 1042 -3.7; 1146 -4.6; 1261 -5.5; 1387 -6.2; 1526 -6.4; 1678 -6.1; 1846 -5.8; 2031 -6.0; 2234 -6.6; 2457 -5.8; 2703 -3.7; 2973 -2.1; 3270 -1.3; 3597 -1.0; 3957 -0.5; 4353 -2.3; 4788 -4.9; 5267 -7.5; 5793 -9.1; 6373 -9.5; 7010 -8.3; 7711 -7.2; 8482 -4.7; 9330 -4.8; 10263 -4.8; 11289 -4.8; 12418 -4.8; 13660 -8.5; 15026 -11.0; 16529 -6.8; 18182 -4.8; 20000 -4.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Soranic SP3 SE GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Soranic SP3 SE ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 114 Hz   | 0.7  | -2.0 dB |
| Peaking | 717 Hz   | 1.97 | 1.9 dB  |
| Peaking | 3815 Hz  | 2.93 | 5.5 dB  |
| Peaking | 6099 Hz  | 2.49 | -5.5 dB |
| Peaking | 14979 Hz | 3.26 | -7.1 dB |
| Peaking | 963 Hz   | 3.58 | 1.6 dB  |
| Peaking | 1956 Hz  | 0.97 | -2.1 dB |
| Peaking | 3006 Hz  | 4.43 | 2.7 dB  |
| Peaking | 10373 Hz | 1.81 | 0.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.1 dB |
| Peaking | 62 Hz    | 1.41 | -0.9 dB |
| Peaking | 125 Hz   | 1.41 | -1.9 dB |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.3 dB |
| Peaking | 4000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.1 dB |
| Peaking | 16000 Hz | 1.41 | -4.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Soranic%20SP3%20SE/Soranic%20SP3%20SE.png)