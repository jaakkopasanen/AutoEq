# Custom Art FIBAE 3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.0; 23 -6.1; 25 -6.1; 28 -6.2; 31 -6.4; 34 -6.5; 37 -6.6; 41 -6.8; 45 -6.9; 49 -7.1; 54 -7.3; 60 -7.5; 66 -7.8; 72 -8.1; 79 -8.4; 87 -8.8; 96 -9.3; 106 -9.6; 116 -9.9; 128 -10.3; 141 -10.5; 155 -10.8; 170 -10.9; 187 -11.0; 206 -11.0; 227 -11.0; 249 -10.9; 274 -10.8; 302 -10.6; 332 -10.5; 365 -10.2; 402 -10.0; 442 -9.7; 486 -9.4; 535 -9.0; 588 -8.5; 647 -8.0; 712 -7.4; 783 -6.7; 861 -6.0; 947 -5.5; 1042 -5.2; 1146 -5.3; 1261 -5.4; 1387 -5.1; 1526 -4.5; 1678 -3.8; 1846 -3.5; 2031 -4.2; 2234 -6.0; 2457 -9.2; 2703 -11.1; 2973 -9.5; 3270 -5.2; 3597 -4.2; 3957 -7.8; 4353 -5.6; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -7.6; 8482 -11.7; 9330 -8.1; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -9.1; 18182 -14.2; 20000 -22.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Custom Art FIBAE 3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Custom Art FIBAE 3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 225 Hz  | 0.48 | -4.8 dB |
| Peaking | 1820 Hz | 0.87 | 3.5 dB  |
| Peaking | 2680 Hz | 3.83 | -7.6 dB |
| Peaking | 5745 Hz | 2.19 | 6.9 dB  |
| Peaking | 8420 Hz | 4.97 | -7.1 dB |
| Peaking | 23 Hz   | 0.97 | 0.7 dB  |
| Peaking | 501 Hz  | 4.4  | -0.4 dB |
| Peaking | 3506 Hz | 7.53 | 3.3 dB  |
| Peaking | 4168 Hz | 4.79 | -5.8 dB |
| Peaking | 4613 Hz | 6.94 | 5.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.5 dB  |
| Peaking | 62 Hz    | 1.41 | -0.6 dB |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | -3.9 dB |
| Peaking | 500 Hz   | 1.41 | -2.7 dB |
| Peaking | 1000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.2 dB |
| Peaking | 4000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -3.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Custom%20Art%20FIBAE%203/Custom%20Art%20FIBAE%203.png)