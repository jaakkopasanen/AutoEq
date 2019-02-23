# Beyerdynamic T70p #0002
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.8; 23 -2.1; 25 -2.3; 28 -2.6; 31 -2.9; 34 -3.0; 37 -3.2; 41 -3.5; 45 -3.6; 49 -3.7; 54 -3.9; 60 -4.1; 66 -4.3; 72 -4.2; 79 -4.2; 87 -4.8; 96 -5.7; 106 -6.5; 116 -7.1; 128 -7.7; 141 -8.1; 155 -8.0; 170 -7.2; 187 -7.8; 206 -7.5; 227 -7.1; 249 -6.8; 274 -6.8; 302 -7.1; 332 -7.5; 365 -7.9; 402 -8.2; 442 -7.3; 486 -6.8; 535 -6.5; 588 -6.4; 647 -6.6; 712 -6.7; 783 -6.5; 861 -6.7; 947 -6.7; 1042 -6.6; 1146 -6.6; 1261 -6.6; 1387 -7.0; 1526 -7.4; 1678 -7.7; 1846 -7.4; 2031 -5.9; 2234 -3.2; 2457 -2.0; 2703 -2.5; 2973 -3.2; 3270 -3.3; 3597 -2.9; 3957 -0.5; 4353 -4.7; 4788 -4.4; 5267 -2.0; 5793 -0.9; 6373 -3.8; 7010 -8.4; 7711 -13.2; 8482 -15.6; 9330 -15.7; 10263 -13.1; 11289 -8.1; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic T70p #0002 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T70p #0002 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 27 Hz    | 0.69 | 4.4 dB   |
| Peaking | 3395 Hz  | 1.47 | 4.6 dB   |
| Peaking | 5640 Hz  | 4.48 | 4.2 dB   |
| Peaking | 6185 Hz  | 3.99 | 3.5 dB   |
| Peaking | 8735 Hz  | 2.21 | -11.1 dB |
| Peaking | 147 Hz   | 2.44 | -2.0 dB  |
| Peaking | 381 Hz   | 3.47 | -1.6 dB  |
| Peaking | 2005 Hz  | 1.61 | -3.4 dB  |
| Peaking | 2364 Hz  | 3.62 | 5.2 dB   |
| Peaking | 12189 Hz | 4.84 | 2.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.0 dB  |
| Peaking | 62 Hz    | 1.41 | 2.5 dB  |
| Peaking | 125 Hz   | 1.41 | -1.4 dB |
| Peaking | 250 Hz   | 1.41 | -0.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | -0.1 dB |
| Peaking | 4000 Hz  | 1.41 | 7.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -7.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20T70p%20#0002/Beyerdynamic%20T70p%20#0002.png)