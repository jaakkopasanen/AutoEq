# Cypher Labs Astru IEM
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.1; 25 -1.5; 28 -2.1; 31 -2.6; 34 -3.0; 37 -3.4; 41 -4.0; 45 -4.4; 49 -4.8; 54 -5.3; 60 -5.8; 66 -6.3; 72 -6.8; 79 -7.2; 87 -7.8; 96 -8.3; 106 -8.6; 116 -8.9; 128 -9.3; 141 -9.5; 155 -9.7; 170 -9.9; 187 -9.9; 206 -9.9; 227 -9.8; 249 -9.7; 274 -9.5; 302 -9.3; 332 -9.0; 365 -8.7; 402 -8.3; 442 -7.8; 486 -7.6; 535 -7.2; 588 -6.5; 647 -6.2; 712 -5.9; 783 -5.6; 861 -5.6; 947 -5.8; 1042 -6.2; 1146 -6.5; 1261 -7.0; 1387 -7.8; 1526 -8.8; 1678 -9.8; 1846 -10.6; 2031 -11.3; 2234 -11.0; 2457 -9.1; 2703 -8.2; 2973 -6.7; 3270 -5.0; 3597 -5.4; 3957 -8.0; 4353 -10.1; 4788 -7.8; 5267 -7.1; 5793 -6.6; 6373 -3.9; 7010 -5.3; 7711 -5.7; 8482 -6.0; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Cypher Labs Astru IEM GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Cypher Labs Astru IEM ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 13 Hz   | 0.4  | 6.6 dB  |
| Peaking | 189 Hz  | 0.48 | -4.3 dB |
| Peaking | 1988 Hz | 1.3  | -9.9 dB |
| Peaking | 2077 Hz | 0.46 | 4.7 dB  |
| Peaking | 4391 Hz | 4.68 | -5.5 dB |
| Peaking | 3019 Hz | 2.31 | -0.8 dB |
| Peaking | 3335 Hz | 5.7  | 2.2 dB  |
| Peaking | 5609 Hz | 9.81 | -3.3 dB |
| Peaking | 6183 Hz | 5.2  | 2.3 dB  |
| Peaking | 8776 Hz | 1.37 | -0.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.5 dB  |
| Peaking | 62 Hz    | 1.41 | -0.4 dB |
| Peaking | 125 Hz   | 1.41 | -3.0 dB |
| Peaking | 250 Hz   | 1.41 | -3.6 dB |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.9 dB |
| Peaking | 4000 Hz  | 1.41 | -0.4 dB |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Cypher%20Labs%20Astru%20IEM/Cypher%20Labs%20Astru%20IEM.png)