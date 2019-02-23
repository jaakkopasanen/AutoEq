# Beyerdynamic T50p
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.8; 31 -1.4; 34 -2.1; 37 -2.7; 41 -3.5; 45 -4.1; 49 -4.7; 54 -5.5; 60 -6.2; 66 -5.2; 72 -5.3; 79 -6.6; 87 -7.3; 96 -7.2; 106 -7.2; 116 -7.2; 128 -6.7; 141 -5.9; 155 -3.9; 170 -3.1; 187 -5.6; 206 -7.9; 227 -8.4; 249 -9.2; 274 -10.9; 302 -12.5; 332 -12.3; 365 -11.9; 402 -11.4; 442 -11.2; 486 -10.8; 535 -10.3; 588 -9.9; 647 -9.5; 712 -7.9; 783 -7.6; 861 -7.5; 947 -7.2; 1042 -6.8; 1146 -6.5; 1261 -6.2; 1387 -6.4; 1526 -6.5; 1678 -6.8; 1846 -6.8; 2031 -6.1; 2234 -4.8; 2457 -3.4; 2703 -2.3; 2973 -1.5; 3270 -0.6; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -2.9; 6373 -4.6; 7010 -4.7; 7711 -10.6; 8482 -13.9; 9330 -12.9; 10263 -7.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.9; 18182 -9.6; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic T50p GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T50p ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 25 Hz    |  1.1  | 6.5 dB   |
| Peaking | 170 Hz   |  3.9  | 5.8 dB   |
| Peaking | 353 Hz   |  0.81 | -5.7 dB  |
| Peaking | 4299 Hz  |  0.97 | 7.1 dB   |
| Peaking | 8619 Hz  |  3.22 | -10.2 dB |
| Peaking | 94 Hz    |  3.83 | -1.0 dB  |
| Peaking | 242 Hz   | 10.64 | 1.2 dB   |
| Peaking | 1876 Hz  |  3.83 | -1.8 dB  |
| Peaking | 2835 Hz  |  3.47 | 1.1 dB   |
| Peaking | 18292 Hz |  2.16 | -3.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.3 dB  |
| Peaking | 62 Hz    | 1.41 | -1.2 dB |
| Peaking | 125 Hz   | 1.41 | 1.6 dB  |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | -4.9 dB |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.8 dB |
| Peaking | 4000 Hz  | 1.41 | 9.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Beyerdynamic%20T50p/Beyerdynamic%20T50p.png)