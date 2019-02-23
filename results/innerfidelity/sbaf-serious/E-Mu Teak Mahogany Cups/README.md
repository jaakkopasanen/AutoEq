# E-Mu Teak Mahogany Cups
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.5; 23 -5.2; 25 -5.7; 28 -6.2; 31 -6.5; 34 -6.5; 37 -6.6; 41 -6.6; 45 -6.5; 49 -6.5; 54 -6.3; 60 -6.0; 66 -6.0; 72 -6.3; 79 -6.6; 87 -6.9; 96 -7.1; 106 -7.1; 116 -7.2; 128 -7.3; 141 -7.4; 155 -7.4; 170 -7.2; 187 -7.1; 206 -7.0; 227 -6.7; 249 -6.4; 274 -6.1; 302 -5.7; 332 -5.5; 365 -5.1; 402 -4.7; 442 -4.2; 486 -3.9; 535 -3.6; 588 -3.0; 647 -3.3; 712 -3.7; 783 -3.8; 861 -2.8; 947 -3.2; 1042 -3.4; 1146 -3.3; 1261 -3.3; 1387 -3.5; 1526 -3.8; 1678 -3.8; 1846 -3.5; 2031 -2.7; 2234 -2.2; 2457 -1.2; 2703 -0.7; 2973 -0.5; 3270 -1.1; 3597 -1.2; 3957 -0.9; 4353 -1.9; 4788 -2.6; 5267 -3.0; 5793 -2.4; 6373 -1.7; 7010 -1.3; 7711 -3.4; 8482 -3.7; 9330 -5.2; 10263 -5.1; 11289 -3.7; 12418 -3.7; 13660 -4.6; 15026 -3.7; 16529 -3.7; 18182 -3.7; 20000 -3.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`E-Mu Teak Mahogany Cups GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `E-Mu Teak Mahogany Cups ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 37 Hz    | 0.83 | -2.4 dB |
| Peaking | 149 Hz   | 0.71 | -3.6 dB |
| Peaking | 3116 Hz  | 1.42 | 3.2 dB  |
| Peaking | 6720 Hz  | 6.45 | 2.6 dB  |
| Peaking | 9742 Hz  | 6.32 | -2.6 dB |
| Peaking | 590 Hz   | 4.72 | 1.1 dB  |
| Peaking | 901 Hz   | 4.42 | 0.8 dB  |
| Peaking | 1711 Hz  | 3.68 | -0.8 dB |
| Peaking | 2557 Hz  | 9.18 | 0.7 dB  |
| Peaking | 13699 Hz | 7.27 | -0.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.5 dB |
| Peaking | 62 Hz    | 1.41 | -1.6 dB |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/E-Mu%20Teak%20Mahogany%20Cups/E-Mu%20Teak%20Mahogany%20Cups.png)