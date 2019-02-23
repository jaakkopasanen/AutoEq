# Oppo PM3 sample A
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.1; 23 -7.2; 25 -7.2; 28 -7.2; 31 -7.1; 34 -7.2; 37 -7.2; 41 -7.1; 45 -7.1; 49 -7.1; 54 -7.1; 60 -7.1; 66 -7.1; 72 -7.2; 79 -7.3; 87 -7.4; 96 -7.8; 106 -7.8; 116 -7.6; 128 -7.4; 141 -7.5; 155 -8.0; 170 -6.9; 187 -7.1; 206 -7.4; 227 -7.0; 249 -6.5; 274 -5.9; 302 -5.5; 332 -5.3; 365 -5.5; 402 -5.8; 442 -6.1; 486 -6.7; 535 -7.0; 588 -7.0; 647 -7.2; 712 -7.5; 783 -7.3; 861 -7.5; 947 -7.7; 1042 -8.0; 1146 -8.2; 1261 -8.4; 1387 -9.1; 1526 -9.8; 1678 -10.9; 1846 -11.7; 2031 -11.1; 2234 -11.1; 2457 -10.4; 2703 -9.3; 2973 -7.6; 3270 -7.1; 3597 -6.9; 3957 -6.0; 4353 -6.0; 4788 -3.7; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Oppo PM3 sample A GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oppo PM3 sample A ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 146 Hz  | 0.76 | -0.6 dB |
| Peaking | 200 Hz  | 0.05 | -0.6 dB |
| Peaking | 330 Hz  | 1.85 | 2.1 dB  |
| Peaking | 1951 Hz | 1.6  | -4.8 dB |
| Peaking | 5714 Hz | 2.72 | 7.4 dB  |
| Peaking | 2459 Hz | 6.76 | -0.8 dB |
| Peaking | 7785 Hz | 8.1  | -1.0 dB |
| Peaking | 9061 Hz | 3.27 | -0.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.8 dB |
| Peaking | 62 Hz    | 1.41 | -0.3 dB |
| Peaking | 125 Hz   | 1.41 | -1.4 dB |
| Peaking | 250 Hz   | 1.41 | 0.5 dB  |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | -5.9 dB |
| Peaking | 4000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Oppo%20PM3%20sample%20A/Oppo%20PM3%20sample%20A.png)