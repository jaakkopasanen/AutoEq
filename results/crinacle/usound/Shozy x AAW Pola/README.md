# Shozy x AAW Pola
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.0; 23 -9.3; 25 -9.5; 28 -9.8; 31 -9.9; 34 -10.1; 37 -10.2; 41 -10.3; 45 -10.4; 49 -10.5; 54 -10.6; 60 -10.7; 66 -10.9; 72 -11.1; 79 -11.3; 87 -11.5; 96 -11.8; 106 -12.0; 116 -12.1; 128 -12.3; 141 -12.4; 155 -12.4; 170 -12.3; 187 -12.2; 206 -12.0; 227 -11.8; 249 -11.6; 274 -11.4; 302 -11.3; 332 -11.1; 365 -11.1; 402 -11.1; 442 -11.0; 486 -11.0; 535 -10.9; 588 -10.8; 647 -10.7; 712 -10.6; 783 -10.1; 861 -9.8; 947 -9.9; 1042 -10.1; 1146 -10.7; 1261 -11.2; 1387 -11.0; 1526 -9.9; 1678 -7.7; 1846 -5.0; 2031 -2.3; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.6; 4353 -2.2; 4788 -0.6; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -8.4; 13660 -9.3; 15026 -10.0; 16529 -13.2; 18182 -13.4; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shozy x AAW Pola GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shozy x AAW Pola ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 173 Hz   | 0.16 | -5.5 dB |
| Peaking | 1429 Hz  | 1.59 | -7.3 dB |
| Peaking | 2412 Hz  | 0.8  | 8.8 dB  |
| Peaking | 5629 Hz  | 2.57 | 4.6 dB  |
| Peaking | 17282 Hz | 1.04 | -7.8 dB |
| Peaking | 20 Hz    | 1.51 | -0.5 dB |
| Peaking | 147 Hz   | 3.57 | -0.6 dB |
| Peaking | 2747 Hz  | 6.03 | -0.9 dB |
| Peaking | 4791 Hz  | 0.5  | 0.4 dB  |
| Peaking | 7953 Hz  | 4.74 | -1.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.2 dB |
| Peaking | 62 Hz    | 1.41 | -3.1 dB |
| Peaking | 125 Hz   | 1.41 | -4.8 dB |
| Peaking | 250 Hz   | 1.41 | -4.0 dB |
| Peaking | 500 Hz   | 1.41 | -2.8 dB |
| Peaking | 1000 Hz  | 1.41 | -5.2 dB |
| Peaking | 2000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -7.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Shozy%20x%20AAW%20Pola/Shozy%20x%20AAW%20Pola.png)