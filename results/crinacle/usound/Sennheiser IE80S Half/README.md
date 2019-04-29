# Sennheiser IE80S Half
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.0; 23 -8.3; 25 -8.6; 28 -9.0; 31 -9.3; 34 -9.5; 37 -9.6; 41 -9.8; 45 -10.0; 49 -10.1; 54 -10.3; 60 -10.4; 66 -10.6; 72 -10.8; 79 -11.0; 87 -11.1; 96 -11.3; 106 -11.4; 116 -11.4; 128 -11.4; 141 -11.3; 155 -11.2; 170 -11.0; 187 -10.7; 206 -10.3; 227 -9.9; 249 -9.5; 274 -9.0; 302 -8.5; 332 -8.0; 365 -7.5; 402 -7.0; 442 -6.6; 486 -6.1; 535 -5.6; 588 -5.2; 647 -4.7; 712 -4.3; 783 -3.8; 861 -3.4; 947 -3.2; 1042 -3.0; 1146 -3.5; 1261 -4.1; 1387 -4.3; 1526 -4.1; 1678 -3.5; 1846 -2.9; 2031 -2.6; 2234 -2.5; 2457 -2.8; 2703 -3.4; 2973 -4.1; 3270 -4.7; 3597 -5.1; 3957 -5.9; 4353 -7.9; 4788 -10.9; 5267 -8.7; 5793 -3.1; 6373 -0.5; 7010 -3.4; 7711 -5.6; 8482 -5.9; 9330 -5.9; 10263 -5.9; 11289 -5.9; 12418 -5.9; 13660 -5.9; 15026 -5.9; 16529 -5.9; 18182 -6.2; 20000 -15.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser IE80S Half GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser IE80S Half ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 37 Hz    | 0.49 | -2.4 dB  |
| Peaking | 150 Hz   | 0.44 | -5.1 dB  |
| Peaking | 1345 Hz  | 0.33 | 3.1 dB   |
| Peaking | 4917 Hz  | 3.77 | -7.4 dB  |
| Peaking | 6276 Hz  | 4.98 | 6.4 dB   |
| Peaking | 1002 Hz  | 1.62 | 2.2 dB   |
| Peaking | 1406 Hz  | 0.97 | -2.8 dB  |
| Peaking | 2071 Hz  | 1.93 | 2.3 dB   |
| Peaking | 18169 Hz | 1.33 | 3.1 dB   |
| Peaking | 20000 Hz | 0.98 | -10.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.9 dB |
| Peaking | 62 Hz    | 1.41 | -3.6 dB |
| Peaking | 125 Hz   | 1.41 | -4.9 dB |
| Peaking | 250 Hz   | 1.41 | -3.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.6 dB |
| Peaking | 8000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Sennheiser%20IE80S%20Half/Sennheiser%20IE80S%20Half.png)