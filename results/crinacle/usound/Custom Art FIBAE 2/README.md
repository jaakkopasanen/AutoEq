# Custom Art FIBAE 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.0; 23 -5.2; 25 -5.4; 28 -5.6; 31 -5.8; 34 -6.0; 37 -6.2; 41 -6.5; 45 -6.6; 49 -6.8; 54 -7.0; 60 -7.3; 66 -7.6; 72 -7.9; 79 -8.3; 87 -8.7; 96 -9.1; 106 -9.5; 116 -9.7; 128 -10.0; 141 -10.3; 155 -10.5; 170 -10.6; 187 -10.6; 206 -10.6; 227 -10.5; 249 -10.3; 274 -10.1; 302 -9.9; 332 -9.6; 365 -9.2; 402 -8.9; 442 -8.5; 486 -8.1; 535 -7.7; 588 -7.2; 647 -6.7; 712 -6.2; 783 -5.7; 861 -5.4; 947 -5.3; 1042 -5.7; 1146 -6.7; 1261 -7.8; 1387 -9.0; 1526 -9.9; 1678 -10.9; 1846 -11.8; 2031 -10.3; 2234 -7.0; 2457 -4.7; 2703 -2.7; 2973 -1.7; 3270 -2.6; 3597 -5.0; 3957 -2.0; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -7.7; 10263 -6.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Custom Art FIBAE 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Custom Art FIBAE 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.93 | 1.6 dB  |
| Peaking | 182 Hz  | 0.65 | -4.4 dB |
| Peaking | 1821 Hz | 2.98 | -6.4 dB |
| Peaking | 2834 Hz | 3.15 | 4.6 dB  |
| Peaking | 5143 Hz | 1.9  | 6.8 dB  |
| Peaking | 910 Hz  | 2.48 | 2.1 dB  |
| Peaking | 1395 Hz | 4.98 | -1.4 dB |
| Peaking | 6350 Hz | 7.03 | 2.0 dB  |
| Peaking | 6656 Hz | 5.75 | 0.9 dB  |
| Peaking | 8442 Hz | 1.62 | -1.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.1 dB  |
| Peaking | 62 Hz    | 1.41 | -0.5 dB |
| Peaking | 125 Hz   | 1.41 | -3.1 dB |
| Peaking | 250 Hz   | 1.41 | -3.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.9 dB |
| Peaking | 4000 Hz  | 1.41 | 7.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Custom%20Art%20FIBAE%202/Custom%20Art%20FIBAE%202.png)