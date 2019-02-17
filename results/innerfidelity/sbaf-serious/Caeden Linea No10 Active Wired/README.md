# Caeden Linea No10 Active Wired
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.4; 23 -9.0; 25 -9.4; 28 -9.9; 31 -10.2; 34 -10.5; 37 -10.7; 41 -11.0; 45 -11.1; 49 -11.2; 54 -11.2; 60 -11.4; 66 -11.7; 72 -12.1; 79 -12.4; 87 -12.6; 96 -12.9; 106 -12.8; 116 -12.7; 128 -12.4; 141 -12.1; 155 -11.9; 170 -10.9; 187 -10.5; 206 -9.6; 227 -8.4; 249 -8.2; 274 -7.9; 302 -7.4; 332 -6.7; 365 -6.0; 402 -5.5; 442 -4.9; 486 -4.7; 535 -4.5; 588 -4.3; 647 -4.5; 712 -5.0; 783 -5.3; 861 -5.8; 947 -6.3; 1042 -6.6; 1146 -6.8; 1261 -7.2; 1387 -7.7; 1526 -8.2; 1678 -8.0; 1846 -7.2; 2031 -6.5; 2234 -5.2; 2457 -3.5; 2703 -2.2; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.0; 4788 -3.8; 5267 -2.8; 5793 -1.7; 6373 -3.6; 7010 -4.4; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Caeden Linea No10 Active Wired GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Caeden Linea No10 Active Wired ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 42 Hz   | 0.56 | -3.4 dB |
| Peaking | 119 Hz  | 0.81 | -5.2 dB |
| Peaking | 514 Hz  | 1.69 | 2.8 dB  |
| Peaking | 3481 Hz | 2.02 | 6.8 dB  |
| Peaking | 5811 Hz | 3.94 | 3.7 dB  |
| Peaking | 735 Hz  | 3.12 | 0.7 dB  |
| Peaking | 1606 Hz | 1.91 | -2.4 dB |
| Peaking | 2691 Hz | 4.33 | 1.8 dB  |
| Peaking | 6995 Hz | 4.72 | 1.1 dB  |
| Peaking | 7838 Hz | 2.55 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.1 dB |
| Peaking | 62 Hz    | 1.41 | -4.1 dB |
| Peaking | 125 Hz   | 1.41 | -5.8 dB |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | 2.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB |
| Peaking | 2000 Hz  | 1.41 | -1.0 dB |
| Peaking | 4000 Hz  | 1.41 | 7.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Caeden%20Linea%20No10%20Active%20Wired/Caeden%20Linea%20No10%20Active%20Wired.png)