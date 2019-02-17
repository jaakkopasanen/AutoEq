# Noontec Hammo Go
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.7; 37 -1.2; 41 -2.0; 45 -2.7; 49 -3.0; 54 -3.6; 60 -4.6; 66 -5.2; 72 -5.8; 79 -6.4; 87 -7.1; 96 -7.8; 106 -8.6; 116 -9.2; 128 -9.5; 141 -9.4; 155 -9.6; 170 -10.0; 187 -10.6; 206 -11.0; 227 -11.2; 249 -11.1; 274 -10.8; 302 -10.6; 332 -10.7; 365 -10.8; 402 -10.4; 442 -8.6; 486 -7.9; 535 -7.5; 588 -6.9; 647 -6.2; 712 -6.8; 783 -6.6; 861 -7.0; 947 -7.0; 1042 -6.1; 1146 -5.0; 1261 -4.4; 1387 -3.7; 1526 -3.4; 1678 -3.0; 1846 -2.8; 2031 -3.2; 2234 -3.6; 2457 -4.3; 2703 -4.8; 2973 -5.7; 3270 -7.8; 3597 -11.7; 3957 -8.8; 4353 -7.1; 4788 -10.3; 5267 -10.4; 5793 -11.0; 6373 -8.3; 7010 -9.2; 7711 -14.4; 8482 -16.6; 9330 -12.4; 10263 -8.3; 11289 -9.2; 12418 -9.2; 13660 -6.6; 15026 -6.7; 16529 -12.6; 18182 -16.2; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Noontec Hammo Go GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noontec Hammo Go ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 27 Hz    | 0.69 | 6.5 dB   |
| Peaking | 164 Hz   | 0.84 | -4.0 dB  |
| Peaking | 327 Hz   | 1.91 | -3.2 dB  |
| Peaking | 8302 Hz  | 2.65 | -9.8 dB  |
| Peaking | 18025 Hz | 1.77 | -10.9 dB |
| Peaking | 1857 Hz  | 1.28 | 4.1 dB   |
| Peaking | 3621 Hz  | 7.94 | -5.7 dB  |
| Peaking | 5467 Hz  | 2.87 | -3.8 dB  |
| Peaking | 6699 Hz  | 6.59 | 3.8 dB   |
| Peaking | 14610 Hz | 4.79 | 2.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | 1.0 dB  |
| Peaking | 125 Hz   | 1.41 | -2.6 dB |
| Peaking | 250 Hz   | 1.41 | -4.8 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.6 dB |
| Peaking | 8000 Hz  | 1.41 | -6.3 dB |
| Peaking | 16000 Hz | 1.41 | -4.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Noontec%20Hammo%20Go/Noontec%20Hammo%20Go.png)