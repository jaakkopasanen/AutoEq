# Astrotec AX35
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.8; 45 -1.5; 49 -2.2; 54 -2.9; 60 -3.8; 66 -4.7; 72 -5.4; 79 -6.2; 87 -7.0; 96 -7.8; 106 -8.5; 116 -9.0; 128 -9.5; 141 -10.0; 155 -10.5; 170 -10.7; 187 -10.9; 206 -11.1; 227 -11.1; 249 -11.1; 274 -11.0; 302 -10.8; 332 -10.6; 365 -10.3; 402 -10.0; 442 -9.5; 486 -9.2; 535 -8.7; 588 -8.0; 647 -7.5; 712 -7.2; 783 -6.6; 861 -6.5; 947 -6.5; 1042 -6.6; 1146 -6.9; 1261 -7.5; 1387 -8.4; 1526 -9.3; 1678 -9.5; 1846 -9.1; 2031 -8.5; 2234 -7.8; 2457 -6.4; 2703 -5.3; 2973 -2.7; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.2; 4788 -2.0; 5267 -2.0; 5793 -3.7; 6373 -6.8; 7010 -4.8; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Astrotec AX35 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Astrotec AX35 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.6  | 6.9 dB  |
| Peaking | 201 Hz  | 0.56 | -5.3 dB |
| Peaking | 1886 Hz | 1.85 | -4.0 dB |
| Peaking | 3769 Hz | 1.47 | 7.0 dB  |
| Peaking | 891 Hz  | 2.49 | 1.2 dB  |
| Peaking | 1487 Hz | 6.68 | -1.0 dB |
| Peaking | 4460 Hz | 2.96 | -0.6 dB |
| Peaking | 5324 Hz | 5.12 | 2.0 dB  |
| Peaking | 6298 Hz | 9.26 | -2.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.5 dB  |
| Peaking | 62 Hz    | 1.41 | 1.8 dB  |
| Peaking | 125 Hz   | 1.41 | -3.1 dB |
| Peaking | 250 Hz   | 1.41 | -4.5 dB |
| Peaking | 500 Hz   | 1.41 | -1.7 dB |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.9 dB |
| Peaking | 4000 Hz  | 1.41 | 7.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Astrotec%20AX35/Astrotec%20AX35.png)