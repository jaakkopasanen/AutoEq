# Sony MH755 sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.5; 23 -10.2; 25 -9.9; 28 -9.6; 31 -9.2; 34 -8.8; 37 -8.5; 41 -8.0; 45 -7.6; 49 -7.2; 54 -6.8; 60 -6.4; 66 -6.1; 72 -5.8; 79 -5.6; 87 -5.4; 96 -5.3; 106 -5.2; 116 -5.0; 128 -4.9; 141 -4.8; 155 -4.5; 170 -4.3; 187 -4.0; 206 -3.8; 227 -3.5; 249 -3.3; 274 -3.0; 302 -2.8; 332 -2.5; 365 -2.3; 402 -2.1; 442 -1.9; 486 -1.7; 535 -1.5; 588 -1.3; 647 -1.1; 712 -0.9; 783 -0.6; 861 -0.5; 947 -0.5; 1042 -0.9; 1146 -1.7; 1261 -2.6; 1387 -3.1; 1526 -3.2; 1678 -3.1; 1846 -2.9; 2031 -2.9; 2234 -3.2; 2457 -3.7; 2703 -4.7; 2973 -5.6; 3270 -5.7; 3597 -5.2; 3957 -4.5; 4353 -3.9; 4788 -3.0; 5267 -2.3; 5793 -2.0; 6373 -2.1; 7010 -3.5; 7711 -3.5; 8482 -2.8; 9330 -2.8; 10263 -2.8; 11289 -2.8; 12418 -2.8; 13660 -4.7; 15026 -4.6; 16529 -4.6; 18182 -4.8; 20000 -2.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MH755 sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MH755 sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 0.69 | -6.6 dB |
| Peaking | 66 Hz    | 0.4  | -2.1 dB |
| Peaking | 735 Hz   | 1.09 | 2.4 dB  |
| Peaking | 3173 Hz  | 2.47 | -3.2 dB |
| Peaking | 16844 Hz | 1.07 | -2.3 dB |
| Peaking | 998 Hz   | 4.93 | 0.8 dB  |
| Peaking | 1413 Hz  | 4.07 | -1.0 dB |
| Peaking | 5785 Hz  | 3.3  | 1.9 dB  |
| Peaking | 9317 Hz  | 0.74 | -2.0 dB |
| Peaking | 10296 Hz | 1.36 | 2.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.4 dB |
| Peaking | 62 Hz    | 1.41 | -1.9 dB |
| Peaking | 125 Hz   | 1.41 | -1.7 dB |
| Peaking | 250 Hz   | 1.41 | -0.4 dB |
| Peaking | 500 Hz   | 1.41 | 1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.1 dB |
| Peaking | 4000 Hz  | 1.41 | -1.7 dB |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -2.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Sony%20MH755%20sample%202/Sony%20MH755%20sample%202.png)