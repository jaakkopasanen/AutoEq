# Sony WI-SP500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.7; 79 -1.8; 87 -3.1; 96 -4.2; 106 -5.3; 116 -6.2; 128 -7.0; 141 -7.6; 155 -8.0; 170 -8.3; 187 -8.6; 206 -8.7; 227 -8.9; 249 -9.0; 274 -9.1; 302 -9.2; 332 -9.3; 365 -9.5; 402 -9.6; 442 -9.6; 486 -9.4; 535 -9.2; 588 -8.7; 647 -8.0; 712 -6.9; 783 -5.7; 861 -4.7; 947 -4.4; 1042 -4.6; 1146 -4.7; 1261 -4.6; 1387 -4.2; 1526 -3.7; 1678 -3.6; 1846 -4.0; 2031 -4.7; 2234 -5.2; 2457 -5.2; 2703 -4.4; 2973 -2.8; 3270 -1.6; 3597 -1.4; 3957 -2.0; 4353 -3.8; 4788 -6.7; 5267 -11.4; 5793 -10.8; 6373 -6.6; 7010 -4.9; 7711 -6.5; 8482 -8.1; 9330 -6.6; 10263 -6.5; 11289 -6.5; 12418 -7.1; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony WI-SP500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony WI-SP500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 50 Hz   | 0.43 | 9.1 dB  |
| Peaking | 260 Hz  | 0.21 | -5.3 dB |
| Peaking | 1115 Hz | 0.75 | 5.2 dB  |
| Peaking | 3628 Hz | 2.2  | 5.4 dB  |
| Peaking | 5438 Hz | 5.96 | -7.7 dB |
| Peaking | 19 Hz   | 1.59 | 2.1 dB  |
| Peaking | 59 Hz   | 0.78 | -1.7 dB |
| Peaking | 71 Hz   | 2.25 | 2.7 dB  |
| Peaking | 7042 Hz | 6.98 | 2.2 dB  |
| Peaking | 8399 Hz | 5.87 | -1.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.9 dB  |
| Peaking | 62 Hz    | 1.41 | 5.9 dB  |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | -3.3 dB |
| Peaking | 1000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sony%20WI-SP500/Sony%20WI-SP500.png)