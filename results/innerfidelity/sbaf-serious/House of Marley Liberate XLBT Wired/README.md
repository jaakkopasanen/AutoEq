# House of Marley Liberate XLBT Wired
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.4; 23 -6.5; 25 -6.6; 28 -6.7; 31 -6.8; 34 -6.8; 37 -6.8; 41 -6.9; 45 -7.0; 49 -7.1; 54 -7.1; 60 -7.2; 66 -7.4; 72 -7.6; 79 -7.9; 87 -8.1; 96 -8.4; 106 -8.6; 116 -8.7; 128 -8.9; 141 -9.3; 155 -9.5; 170 -9.5; 187 -9.6; 206 -9.9; 227 -10.3; 249 -10.4; 274 -10.4; 302 -10.3; 332 -10.2; 365 -9.9; 402 -9.4; 442 -8.3; 486 -7.2; 535 -5.9; 588 -3.9; 647 -2.7; 712 -3.0; 783 -3.7; 861 -5.3; 947 -6.3; 1042 -6.9; 1146 -7.4; 1261 -7.6; 1387 -7.6; 1526 -7.2; 1678 -5.8; 1846 -4.6; 2031 -1.2; 2234 -0.6; 2457 -2.1; 2703 -2.2; 2973 -1.6; 3270 -1.3; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`House of Marley Liberate XLBT Wired GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `House of Marley Liberate XLBT Wired ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 384 Hz  | 0.35 | -4.9 dB |
| Peaking | 663 Hz  | 1.63 | 8.1 dB  |
| Peaking | 1609 Hz | 1.54 | -3.6 dB |
| Peaking | 2123 Hz | 1.58 | 6.9 dB  |
| Peaking | 4648 Hz | 1.28 | 6.4 dB  |
| Peaking | 3534 Hz | 4.02 | 1.7 dB  |
| Peaking | 4644 Hz | 1.37 | -1.5 dB |
| Peaking | 6335 Hz | 2.74 | 3.8 dB  |
| Peaking | 7547 Hz | 3.37 | -2.2 dB |
| Peaking | 9031 Hz | 1.18 | -0.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.0 dB  |
| Peaking | 62 Hz    | 1.41 | -0.6 dB |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | -4.8 dB |
| Peaking | 500 Hz   | 1.41 | 1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/House%20of%20Marley%20Liberate%20XLBT%20Wired/House%20of%20Marley%20Liberate%20XLBT%20Wired.png)