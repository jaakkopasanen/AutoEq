# Audeze LCD-2 Classic
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.9; 23 -2.0; 25 -2.1; 28 -2.5; 31 -3.0; 34 -3.4; 37 -3.8; 41 -4.1; 45 -4.2; 49 -4.3; 54 -4.3; 60 -4.4; 66 -4.7; 72 -4.9; 79 -5.1; 87 -5.5; 96 -5.8; 106 -6.2; 116 -6.6; 128 -6.9; 141 -7.3; 155 -7.4; 170 -7.5; 187 -7.6; 206 -7.6; 227 -7.7; 249 -7.8; 274 -8.0; 302 -8.1; 332 -8.2; 365 -8.3; 402 -8.5; 442 -8.5; 486 -8.2; 535 -8.1; 588 -8.7; 647 -9.1; 712 -9.5; 783 -9.9; 861 -10.2; 947 -9.1; 1042 -8.4; 1146 -8.7; 1261 -8.4; 1387 -8.0; 1526 -6.5; 1678 -7.0; 1846 -6.7; 2031 -6.9; 2234 -5.2; 2457 -5.6; 2703 -4.0; 2973 -3.8; 3270 -1.4; 3597 -0.5; 3957 -0.5; 4353 -1.8; 4788 -2.8; 5267 -2.7; 5793 -5.3; 6373 -7.3; 7010 -6.2; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.8; 15026 -7.7; 16529 -9.2; 18182 -10.8; 20000 -12.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-2 Classic GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-2 Classic ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 0.84 | 4.5 dB  |
| Peaking | 68 Hz    | 0.99 | 1.8 dB  |
| Peaking | 408 Hz   | 0.21 | -1.7 dB |
| Peaking | 827 Hz   | 2.27 | -2.2 dB |
| Peaking | 3782 Hz  | 1.85 | 6.8 dB  |
| Peaking | 5177 Hz  | 9.27 | 2.3 dB  |
| Peaking | 11451 Hz | 1.23 | 2.5 dB  |
| Peaking | 15626 Hz | 1.3  | 2.4 dB  |
| Peaking | 19366 Hz | 0.17 | -5.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.9 dB  |
| Peaking | 62 Hz    | 1.41 | 1.5 dB  |
| Peaking | 125 Hz   | 1.41 | -0.5 dB |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.6 dB |
| Peaking | 1000 Hz  | 1.41 | -2.9 dB |
| Peaking | 2000 Hz  | 1.41 | -0.2 dB |
| Peaking | 4000 Hz  | 1.41 | 6.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | -3.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audeze%20LCD-2%20Classic/Audeze%20LCD-2%20Classic.png)