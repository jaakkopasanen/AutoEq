# 1MORE Piston Classic
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.6; 25 -0.8; 28 -1.4; 31 -2.1; 34 -2.6; 37 -3.1; 41 -3.7; 45 -4.2; 49 -4.7; 54 -5.4; 60 -6.3; 66 -7.0; 72 -7.7; 79 -8.4; 87 -9.3; 96 -10.1; 106 -11.0; 116 -11.8; 128 -12.6; 141 -13.3; 155 -13.7; 170 -14.0; 187 -14.3; 206 -14.3; 227 -14.3; 249 -14.0; 274 -13.9; 302 -13.7; 332 -13.3; 365 -12.8; 402 -12.2; 442 -11.5; 486 -10.7; 535 -9.7; 588 -8.6; 647 -7.7; 712 -6.8; 783 -6.5; 861 -6.5; 947 -6.6; 1042 -6.2; 1146 -5.7; 1261 -5.4; 1387 -4.8; 1526 -4.0; 1678 -3.2; 1846 -2.4; 2031 -1.8; 2234 -1.0; 2457 -0.5; 2703 -1.0; 2973 -3.2; 3270 -6.5; 3597 -8.6; 3957 -9.2; 4353 -10.0; 4788 -10.1; 5267 -10.3; 5793 -10.0; 6373 -9.4; 7010 -6.9; 7711 -6.2; 8482 -6.5; 9330 -7.3; 10263 -7.2; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -7.3; 18182 -8.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`1MORE Piston Classic GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `1MORE Piston Classic ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 0.46 | 6.4 dB  |
| Peaking | 205 Hz   | 0.52 | -8.5 dB |
| Peaking | 2653 Hz  | 0.95 | 11.1 dB |
| Peaking | 3903 Hz  | 1.05 | -9.9 dB |
| Peaking | 18009 Hz | 2.44 | -2.4 dB |
| Peaking | 408 Hz   | 2.84 | -0.9 dB |
| Peaking | 709 Hz   | 3.55 | 1.5 dB  |
| Peaking | 4144 Hz  | 6.6  | 1.0 dB  |
| Peaking | 6332 Hz  | 2.39 | -2.4 dB |
| Peaking | 7329 Hz  | 3.56 | 3.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.8 dB  |
| Peaking | 62 Hz    | 1.41 | 0.1 dB  |
| Peaking | 125 Hz   | 1.41 | -5.3 dB |
| Peaking | 250 Hz   | 1.41 | -7.5 dB |
| Peaking | 500 Hz   | 1.41 | -2.5 dB |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | 6.9 dB  |
| Peaking | 4000 Hz  | 1.41 | -4.0 dB |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/1MORE%20Piston%20Classic/1MORE%20Piston%20Classic.png)