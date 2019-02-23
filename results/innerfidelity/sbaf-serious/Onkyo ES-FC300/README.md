# Onkyo ES-FC300
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.9; 23 -11.1; 25 -11.3; 28 -11.4; 31 -11.4; 34 -11.3; 37 -11.4; 41 -11.5; 45 -11.7; 49 -11.9; 54 -11.8; 60 -11.4; 66 -10.9; 72 -10.4; 79 -11.1; 87 -12.0; 96 -12.2; 106 -11.6; 116 -11.9; 128 -12.3; 141 -12.2; 155 -11.8; 170 -11.0; 187 -10.5; 206 -9.1; 227 -7.9; 249 -6.7; 274 -6.5; 302 -7.8; 332 -8.6; 365 -9.2; 402 -9.4; 442 -9.2; 486 -9.0; 535 -8.7; 588 -8.2; 647 -8.0; 712 -7.7; 783 -7.2; 861 -6.9; 947 -6.5; 1042 -6.3; 1146 -6.0; 1261 -5.7; 1387 -5.7; 1526 -6.1; 1678 -6.4; 1846 -6.3; 2031 -5.9; 2234 -5.7; 2457 -5.5; 2703 -5.9; 2973 -5.2; 3270 -4.6; 3597 -4.1; 3957 -1.0; 4353 -1.4; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Onkyo ES-FC300 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Onkyo ES-FC300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 14 Hz   | 0.5  | -3.6 dB |
| Peaking | 52 Hz   | 0.6  | -3.9 dB |
| Peaking | 135 Hz  | 1.53 | -4.3 dB |
| Peaking | 460 Hz  | 1.96 | -2.7 dB |
| Peaking | 5018 Hz | 1.64 | 6.8 dB  |
| Peaking | 260 Hz  | 1.44 | -1.8 dB |
| Peaking | 261 Hz  | 3.45 | 3.7 dB  |
| Peaking | 1255 Hz | 4.02 | 0.9 dB  |
| Peaking | 6443 Hz | 4.65 | 3.5 dB  |
| Peaking | 7452 Hz | 1.76 | -2.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.2 dB |
| Peaking | 62 Hz    | 1.41 | -3.0 dB |
| Peaking | 125 Hz   | 1.41 | -5.7 dB |
| Peaking | 250 Hz   | 1.41 | 0.4 dB  |
| Peaking | 500 Hz   | 1.41 | -2.9 dB |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.0 dB |
| Peaking | 4000 Hz  | 1.41 | 5.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Onkyo%20ES-FC300/Onkyo%20ES-FC300.png)