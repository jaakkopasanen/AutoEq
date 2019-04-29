# Massdrop x Tanchim Cora
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.8; 23 -7.0; 25 -7.1; 28 -7.2; 31 -7.3; 34 -7.3; 37 -7.3; 41 -7.3; 45 -7.2; 49 -7.2; 54 -7.2; 60 -7.1; 66 -7.1; 72 -7.1; 79 -7.0; 87 -7.0; 96 -7.0; 106 -7.0; 116 -6.8; 128 -6.7; 141 -6.5; 155 -6.1; 170 -5.7; 187 -5.3; 206 -4.8; 227 -4.4; 249 -4.2; 274 -4.0; 302 -3.9; 332 -3.6; 365 -3.4; 402 -3.2; 442 -3.1; 486 -3.0; 535 -3.0; 588 -3.1; 647 -3.3; 712 -3.6; 783 -4.0; 861 -4.5; 947 -5.3; 1042 -6.2; 1146 -7.0; 1261 -8.5; 1387 -9.3; 1526 -8.4; 1678 -7.0; 1846 -5.6; 2031 -4.7; 2234 -4.4; 2457 -4.8; 2703 -5.5; 2973 -4.9; 3270 -3.0; 3597 -1.4; 3957 -0.5; 4353 -1.4; 4788 -3.8; 5267 -3.4; 5793 -0.7; 6373 -0.7; 7010 -3.1; 7711 -4.3; 8482 -4.3; 9330 -4.3; 10263 -4.3; 11289 -4.3; 12418 -4.3; 13660 -4.4; 15026 -6.9; 16529 -6.6; 18182 -4.3; 20000 -4.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop x Tanchim Cora GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x Tanchim Cora ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 48 Hz    | 0.45 | -3.3 dB |
| Peaking | 1387 Hz  | 3.03 | -5.3 dB |
| Peaking | 3917 Hz  | 4.62 | 4.3 dB  |
| Peaking | 6144 Hz  | 5.53 | 4.3 dB  |
| Peaking | 15731 Hz | 3.61 | -4.0 dB |
| Peaking | 134 Hz   | 1.97 | -1.1 dB |
| Peaking | 465 Hz   | 0.77 | 1.5 dB  |
| Peaking | 757 Hz   | 1.58 | 0.9 dB  |
| Peaking | 959 Hz   | 1.38 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.9 dB |
| Peaking | 62 Hz    | 1.41 | -2.1 dB |
| Peaking | 125 Hz   | 1.41 | -2.2 dB |
| Peaking | 250 Hz   | 1.41 | 0.2 dB  |
| Peaking | 500 Hz   | 1.41 | 2.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.3 dB |
| Peaking | 2000 Hz  | 1.41 | -2.4 dB |
| Peaking | 4000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -2.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Massdrop%20x%20Tanchim%20Cora/Massdrop%20x%20Tanchim%20Cora.png)