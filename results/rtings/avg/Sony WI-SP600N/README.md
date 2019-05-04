# Sony WI-SP600N
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.9; 23 -14.2; 25 -14.5; 28 -14.7; 31 -14.9; 34 -15.0; 37 -15.0; 41 -15.0; 45 -14.9; 49 -14.7; 54 -14.4; 60 -14.1; 66 -13.9; 72 -13.6; 79 -13.2; 87 -12.9; 96 -12.5; 106 -12.1; 116 -11.7; 128 -11.2; 141 -10.6; 155 -10.0; 170 -9.5; 187 -9.0; 206 -8.6; 227 -8.0; 249 -7.5; 274 -6.9; 302 -6.4; 332 -5.9; 365 -5.4; 402 -4.9; 442 -4.5; 486 -4.0; 535 -3.5; 588 -2.9; 647 -2.3; 712 -1.7; 783 -1.1; 861 -0.7; 947 -0.6; 1042 -0.6; 1146 -1.7; 1261 -2.8; 1387 -3.3; 1526 -3.5; 1678 -3.5; 1846 -3.5; 2031 -3.5; 2234 -3.0; 2457 -2.2; 2703 -1.8; 2973 -2.0; 3270 -2.6; 3597 -2.6; 3957 -1.7; 4353 -0.8; 4788 -0.7; 5267 -0.5; 5793 -2.6; 6373 -6.7; 7010 -2.4; 7711 -3.7; 8482 -3.9; 9330 -3.9; 10263 -7.7; 11289 -12.3; 12418 -7.1; 13660 -3.9; 15026 -3.9; 16529 -5.4; 18182 -11.2; 20000 -6.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony WI-SP600N GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony WI-SP600N ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 37 Hz    | 0.22 | -11.0 dB |
| Peaking | 853 Hz   | 1.3  | 3.8 dB   |
| Peaking | 4518 Hz  | 1.97 | 3.4 dB   |
| Peaking | 11232 Hz | 5.18 | -9.3 dB  |
| Peaking | 18619 Hz | 1.75 | -8.2 dB  |
| Peaking | 1522 Hz  | 3.15 | -0.7 dB  |
| Peaking | 2654 Hz  | 5.58 | 1.5 dB   |
| Peaking | 6280 Hz  | 7.63 | -6.7 dB  |
| Peaking | 6429 Hz  | 2.66 | 2.6 dB   |
| Peaking | 14987 Hz | 2.85 | 1.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -11.4 dB |
| Peaking | 62 Hz    | 1.41 | -7.6 dB  |
| Peaking | 125 Hz   | 1.41 | -5.6 dB  |
| Peaking | 250 Hz   | 1.41 | -2.6 dB  |
| Peaking | 500 Hz   | 1.41 | 0.5 dB   |
| Peaking | 1000 Hz  | 1.41 | 3.3 dB   |
| Peaking | 2000 Hz  | 1.41 | -0.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.3 dB   |
| Peaking | 8000 Hz  | 1.41 | -1.4 dB  |
| Peaking | 16000 Hz | 1.41 | -3.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20WI-SP600N/Sony%20WI-SP600N.png)