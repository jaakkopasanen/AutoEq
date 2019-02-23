# Caeden Linea No10 Active Wired
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.3; 23 -9.8; 25 -10.2; 28 -10.7; 31 -11.1; 34 -11.4; 37 -11.6; 41 -11.8; 45 -12.0; 49 -12.1; 54 -12.1; 60 -12.3; 66 -12.6; 72 -13.0; 79 -13.3; 87 -13.5; 96 -13.7; 106 -13.7; 116 -13.5; 128 -13.3; 141 -13.0; 155 -12.8; 170 -11.8; 187 -11.3; 206 -10.5; 227 -9.3; 249 -9.1; 274 -8.8; 302 -8.3; 332 -7.6; 365 -6.9; 402 -6.4; 442 -5.8; 486 -5.5; 535 -5.4; 588 -5.1; 647 -5.4; 712 -5.9; 783 -6.2; 861 -6.6; 947 -7.1; 1042 -7.5; 1146 -7.7; 1261 -8.1; 1387 -8.6; 1526 -9.0; 1678 -8.9; 1846 -8.1; 2031 -7.4; 2234 -6.1; 2457 -4.4; 2703 -3.1; 2973 -0.7; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.5; 4788 -4.7; 5267 -3.7; 5793 -2.5; 6373 -4.5; 7010 -5.3; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Caeden Linea No10 Active Wired GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Caeden Linea No10 Active Wired ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 52 Hz   | 0.52 | -4.9 dB |
| Peaking | 129 Hz  | 1.02 | -4.9 dB |
| Peaking | 3527 Hz | 2.39 | 7.0 dB  |
| Peaking | 5806 Hz | 4.7  | 3.0 dB  |
| Peaking | 26 Hz   | 1.59 | -0.7 dB |
| Peaking | 559 Hz  | 1.81 | 2.0 dB  |
| Peaking | 1595 Hz | 1.43 | -3.0 dB |
| Peaking | 2556 Hz | 4.29 | 1.5 dB  |
| Peaking | 2918 Hz | 9.13 | 1.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.0 dB |
| Peaking | 62 Hz    | 1.41 | -4.8 dB |
| Peaking | 125 Hz   | 1.41 | -6.5 dB |
| Peaking | 250 Hz   | 1.41 | -1.9 dB |
| Peaking | 500 Hz   | 1.41 | 2.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.3 dB |
| Peaking | 2000 Hz  | 1.41 | -1.8 dB |
| Peaking | 4000 Hz  | 1.41 | 7.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Caeden%20Linea%20No10%20Active%20Wired/Caeden%20Linea%20No10%20Active%20Wired.png)