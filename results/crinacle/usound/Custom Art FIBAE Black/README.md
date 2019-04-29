# Custom Art FIBAE Black
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.9; 23 -5.3; 25 -5.7; 28 -6.1; 31 -6.5; 34 -6.7; 37 -6.9; 41 -7.1; 45 -7.4; 49 -7.6; 54 -7.9; 60 -8.2; 66 -8.4; 72 -8.8; 79 -9.1; 87 -9.5; 96 -9.9; 106 -10.3; 116 -10.6; 128 -10.9; 141 -11.2; 155 -11.3; 170 -11.5; 187 -11.6; 206 -11.7; 227 -11.6; 249 -11.5; 274 -11.4; 302 -11.3; 332 -11.0; 365 -10.8; 402 -10.4; 442 -10.0; 486 -9.6; 535 -9.0; 588 -8.3; 647 -7.5; 712 -6.6; 783 -5.7; 861 -5.0; 947 -4.8; 1042 -5.1; 1146 -6.0; 1261 -7.1; 1387 -7.6; 1526 -7.5; 1678 -6.9; 1846 -6.2; 2031 -5.5; 2234 -5.1; 2457 -4.9; 2703 -5.0; 2973 -5.3; 3270 -4.2; 3597 -2.0; 3957 -0.6; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -1.3; 6373 -1.3; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Custom Art FIBAE Black GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Custom Art FIBAE Black ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 15 Hz   | 1.04 | 2.7 dB  |
| Peaking | 182 Hz  | 0.58 | -2.1 dB |
| Peaking | 308 Hz  | 0.25 | -3.3 dB |
| Peaking | 865 Hz  | 1.78 | 4.3 dB  |
| Peaking | 4690 Hz | 1.4  | 6.9 dB  |
| Peaking | 1469 Hz | 3.69 | -1.4 dB |
| Peaking | 2906 Hz | 1.07 | 1.8 dB  |
| Peaking | 3011 Hz | 4.41 | -2.5 dB |
| Peaking | 6430 Hz | 3.61 | 4.8 dB  |
| Peaking | 6810 Hz | 1.35 | -3.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.7 dB  |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | -3.6 dB |
| Peaking | 250 Hz   | 1.41 | -4.7 dB |
| Peaking | 500 Hz   | 1.41 | -2.3 dB |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Custom%20Art%20FIBAE%20Black/Custom%20Art%20FIBAE%20Black.png)