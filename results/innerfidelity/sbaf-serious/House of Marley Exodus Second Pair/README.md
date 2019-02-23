# House of Marley Exodus Second Pair
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.6; 31 -0.9; 34 -1.3; 37 -1.8; 41 -2.4; 45 -2.7; 49 -3.0; 54 -3.5; 60 -4.0; 66 -4.3; 72 -4.2; 79 -4.9; 87 -5.4; 96 -6.1; 106 -6.5; 116 -6.8; 128 -7.1; 141 -7.3; 155 -7.4; 170 -7.4; 187 -7.4; 206 -7.2; 227 -8.6; 249 -7.9; 274 -7.2; 302 -7.2; 332 -7.4; 365 -7.4; 402 -7.2; 442 -6.9; 486 -6.9; 535 -6.6; 588 -6.4; 647 -6.8; 712 -7.5; 783 -7.7; 861 -8.1; 947 -8.2; 1042 -7.9; 1146 -7.1; 1261 -6.8; 1387 -6.4; 1526 -6.3; 1678 -5.8; 1846 -5.2; 2031 -4.7; 2234 -4.7; 2457 -4.6; 2703 -5.2; 2973 -6.0; 3270 -6.6; 3597 -6.5; 3957 -5.0; 4353 -4.2; 4788 -4.6; 5267 -4.7; 5793 -4.9; 6373 -7.4; 7010 -9.2; 7711 -7.1; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`House of Marley Exodus Second Pair GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `House of Marley Exodus Second Pair ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 1.2  | 6.3 dB  |
| Peaking | 50 Hz    | 1.88 | 2.2 dB  |
| Peaking | 2230 Hz  | 3.48 | 2.1 dB  |
| Peaking | 5057 Hz  | 2.21 | 2.4 dB  |
| Peaking | 6838 Hz  | 6.42 | -4.0 dB |
| Peaking | 73 Hz    | 4.06 | 1.0 dB  |
| Peaking | 134 Hz   | 1.77 | -0.8 dB |
| Peaking | 240 Hz   | 1.4  | -1.3 dB |
| Peaking | 916 Hz   | 2.9  | -1.9 dB |
| Peaking | 22050 Hz | 1.98 | 0.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.3 dB  |
| Peaking | 62 Hz    | 1.41 | 1.7 dB  |
| Peaking | 125 Hz   | 1.41 | -0.9 dB |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.8 dB |
| Peaking | 2000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/House%20of%20Marley%20Exodus%20Second%20Pair/House%20of%20Marley%20Exodus%20Second%20Pair.png)