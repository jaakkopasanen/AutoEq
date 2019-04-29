# Clear Tune CT-6E sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.8; 23 -5.8; 25 -5.8; 28 -5.9; 31 -6.0; 34 -6.1; 37 -6.1; 41 -6.2; 45 -6.4; 49 -6.5; 54 -6.7; 60 -6.9; 66 -7.2; 72 -7.6; 79 -7.9; 87 -8.3; 96 -8.8; 106 -9.2; 116 -9.6; 128 -9.9; 141 -10.1; 155 -10.4; 170 -10.6; 187 -10.7; 206 -10.7; 227 -10.6; 249 -10.6; 274 -10.4; 302 -10.2; 332 -9.9; 365 -9.5; 402 -9.2; 442 -8.7; 486 -8.1; 535 -7.3; 588 -6.2; 647 -5.0; 712 -3.1; 783 -0.9; 861 -0.5; 947 -0.5; 1042 -0.5; 1146 -0.5; 1261 -3.3; 1387 -7.0; 1526 -9.6; 1678 -11.7; 1846 -13.1; 2031 -12.7; 2234 -11.3; 2457 -9.7; 2703 -8.3; 2973 -7.7; 3270 -7.6; 3597 -7.4; 3957 -8.5; 4353 -7.2; 4788 -3.3; 5267 -1.5; 5793 -0.6; 6373 -1.0; 7010 -4.0; 7711 -7.5; 8482 -8.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Clear Tune CT-6E sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Clear Tune CT-6E sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 274 Hz  | 0.44 | -4.9 dB |
| Peaking | 1001 Hz | 1.07 | 10.4 dB |
| Peaking | 1792 Hz | 1.68 | -9.8 dB |
| Peaking | 5809 Hz | 2.19 | 11.3 dB |
| Peaking | 5913 Hz | 0.84 | -4.4 dB |
| Peaking | 30 Hz   | 0.93 | 1.0 dB  |
| Peaking | 4103 Hz | 6.04 | -4.1 dB |
| Peaking | 4298 Hz | 2.77 | 2.1 dB  |
| Peaking | 8234 Hz | 6.11 | -3.6 dB |
| Peaking | 8831 Hz | 1.42 | 1.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.9 dB  |
| Peaking | 62 Hz    | 1.41 | -0.0 dB |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | -4.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.9 dB |
| Peaking | 1000 Hz  | 1.41 | 9.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -8.8 dB |
| Peaking | 4000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Clear%20Tune%20CT-6E%20sample%201/Clear%20Tune%20CT-6E%20sample%201.png)