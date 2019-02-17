# Nocs NS800
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.8; 23 -5.9; 25 -6.0; 28 -6.1; 31 -6.2; 34 -6.2; 37 -6.3; 41 -6.4; 45 -6.6; 49 -6.6; 54 -6.8; 60 -7.1; 66 -7.4; 72 -7.6; 79 -7.9; 87 -8.3; 96 -8.6; 106 -8.9; 116 -8.9; 128 -9.3; 141 -9.4; 155 -9.5; 170 -9.6; 187 -9.6; 206 -9.5; 227 -9.4; 249 -9.4; 274 -9.1; 302 -9.0; 332 -8.8; 365 -8.5; 402 -8.3; 442 -7.8; 486 -7.7; 535 -7.4; 588 -6.8; 647 -6.5; 712 -6.3; 783 -6.0; 861 -6.1; 947 -6.3; 1042 -6.5; 1146 -6.7; 1261 -6.9; 1387 -7.3; 1526 -7.7; 1678 -7.8; 1846 -7.5; 2031 -7.2; 2234 -7.1; 2457 -6.8; 2703 -7.1; 2973 -6.4; 3270 -3.7; 3597 -0.6; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.8; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Nocs NS800 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Nocs NS800 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 0.63 | 0.7 dB  |
| Peaking | 176 Hz  | 0.61 | -3.3 dB |
| Peaking | 1785 Hz | 2.24 | -2.0 dB |
| Peaking | 2746 Hz | 3.99 | -3.3 dB |
| Peaking | 4448 Hz | 1.22 | 7.2 dB  |
| Peaking | 784 Hz  | 3.21 | 0.9 dB  |
| Peaking | 3637 Hz | 8.32 | 2.0 dB  |
| Peaking | 4388 Hz | 1.91 | -1.0 dB |
| Peaking | 6251 Hz | 2.78 | 5.0 dB  |
| Peaking | 7379 Hz | 1.5  | -3.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.6 dB  |
| Peaking | 62 Hz    | 1.41 | -0.4 dB |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.2 dB |
| Peaking | 4000 Hz  | 1.41 | 7.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Nocs%20NS800/Nocs%20NS800.png)