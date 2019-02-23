# Stax SR-009 SZ9-1278 after burnin
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.9; 23 -0.9; 25 -0.9; 28 -0.8; 31 -0.8; 34 -0.7; 37 -0.8; 41 -0.8; 45 -0.9; 49 -1.4; 54 -2.5; 60 -3.9; 66 -4.3; 72 -4.2; 79 -4.2; 87 -4.3; 96 -4.6; 106 -4.7; 116 -4.8; 128 -5.1; 141 -5.4; 155 -5.5; 170 -5.7; 187 -5.8; 206 -5.9; 227 -5.9; 249 -6.0; 274 -6.1; 302 -6.2; 332 -6.2; 365 -6.3; 402 -6.4; 442 -6.5; 486 -6.9; 535 -7.1; 588 -6.9; 647 -7.3; 712 -7.6; 783 -7.4; 861 -7.5; 947 -8.2; 1042 -8.9; 1146 -9.2; 1261 -9.1; 1387 -9.4; 1526 -9.8; 1678 -10.1; 1846 -8.6; 2031 -7.1; 2234 -6.4; 2457 -4.9; 2703 -5.0; 2973 -5.9; 3270 -6.0; 3597 -5.1; 3957 -6.7; 4353 -7.8; 4788 -9.3; 5267 -6.8; 5793 -0.5; 6373 -1.6; 7010 -5.4; 7711 -6.1; 8482 -6.4; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -7.3; 15026 -6.5; 16529 -6.4; 18182 -6.4; 20000 -9.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-009 SZ9-1278 after burnin GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-009 SZ9-1278 after burnin ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 29 Hz    |  0.52 | 5.9 dB  |
| Peaking | 1689 Hz  |  0.98 | -5.4 dB |
| Peaking | 2387 Hz  |  1.38 | 4.6 dB  |
| Peaking | 4912 Hz  |  4.27 | -4.9 dB |
| Peaking | 5905 Hz  |  4.54 | 7.8 dB  |
| Peaking | 62 Hz    |  1.27 | 1.6 dB  |
| Peaking | 63 Hz    |  2.76 | -2.6 dB |
| Peaking | 3615 Hz  | 13.09 | 1.2 dB  |
| Peaking | 21140 Hz |  0.07 | -0.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.8 dB  |
| Peaking | 62 Hz    | 1.41 | 1.6 dB  |
| Peaking | 125 Hz   | 1.41 | 0.8 dB  |
| Peaking | 250 Hz   | 1.41 | 0.2 dB  |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.6 dB |
| Peaking | 2000 Hz  | 1.41 | -0.9 dB |
| Peaking | 4000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-009%20SZ9-1278%20after%20burnin/Stax%20SR-009%20SZ9-1278%20after%20burnin.png)