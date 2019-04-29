# Noble Audio Khan
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.5; 23 -6.6; 25 -6.8; 28 -6.9; 31 -7.0; 34 -7.0; 37 -7.0; 41 -7.0; 45 -7.0; 49 -7.0; 54 -7.0; 60 -6.9; 66 -7.0; 72 -7.0; 79 -7.1; 87 -7.1; 96 -7.2; 106 -7.3; 116 -7.3; 128 -7.3; 141 -7.3; 155 -7.2; 170 -7.1; 187 -7.1; 206 -6.9; 227 -6.8; 249 -6.8; 274 -6.7; 302 -6.8; 332 -6.8; 365 -6.9; 402 -7.0; 442 -7.2; 486 -7.3; 535 -7.5; 588 -7.7; 647 -7.7; 712 -7.8; 783 -7.8; 861 -7.7; 947 -7.6; 1042 -7.8; 1146 -8.3; 1261 -8.8; 1387 -9.0; 1526 -8.6; 1678 -7.8; 1846 -6.9; 2031 -6.2; 2234 -5.6; 2457 -5.2; 2703 -4.6; 2973 -3.9; 3270 -2.9; 3597 -1.8; 3957 -0.8; 4353 -0.5; 4788 -0.5; 5267 -1.5; 5793 -4.6; 6373 -6.8; 7010 -7.8; 7711 -9.2; 8482 -10.5; 9330 -9.7; 10263 -6.7; 11289 -6.5; 12418 -6.9; 13660 -8.1; 15026 -8.1; 16529 -9.2; 18182 -10.5; 20000 -9.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Noble Audio Khan GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noble Audio Khan ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 221 Hz   | 0.12 | -0.6 dB |
| Peaking | 1366 Hz  | 1.78 | -2.5 dB |
| Peaking | 4404 Hz  | 1.28 | 7.1 dB  |
| Peaking | 7928 Hz  | 1.93 | -5.1 dB |
| Peaking | 18770 Hz | 0.76 | -4.4 dB |
| Peaking | 303 Hz   | 1.96 | 0.5 dB  |
| Peaking | 677 Hz   | 1.79 | -0.6 dB |
| Peaking | 1019 Hz  | 3.57 | 0.4 dB  |
| Peaking | 9122 Hz  | 7.25 | -1.6 dB |
| Peaking | 10701 Hz | 3.55 | 1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.4 dB |
| Peaking | 62 Hz    | 1.41 | -0.3 dB |
| Peaking | 125 Hz   | 1.41 | -0.8 dB |
| Peaking | 250 Hz   | 1.41 | 0.0 dB  |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | -1.8 dB |
| Peaking | 2000 Hz  | 1.41 | -1.5 dB |
| Peaking | 4000 Hz  | 1.41 | 7.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.6 dB |
| Peaking | 16000 Hz | 1.41 | -2.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Noble%20Audio%20Khan/Noble%20Audio%20Khan.png)