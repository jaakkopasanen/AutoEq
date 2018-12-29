# Oppo PM3 sample C
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.5; 25 2.4; 28 2.2; 31 2.2; 34 2.1; 37 2.1; 41 2.0; 45 2.0; 49 2.1; 54 2.0; 60 1.8; 66 1.7; 72 1.7; 79 1.6; 87 1.6; 96 1.1; 106 0.2; 116 -0.4; 128 -1.0; 141 -1.3; 155 -1.0; 170 -0.2; 187 -1.0; 206 -0.5; 227 0.2; 249 0.9; 274 1.8; 302 2.7; 332 3.3; 365 3.6; 402 3.3; 442 2.9; 486 2.0; 535 1.2; 588 1.0; 647 0.5; 712 0.0; 783 0.1; 861 0.1; 947 0.1; 1042 -0.1; 1146 -0.5; 1261 -0.6; 1387 -1.1; 1526 -1.6; 1678 -1.6; 1846 -2.5; 2031 -2.5; 2234 -3.0; 2457 -1.9; 2703 -1.2; 2973 -0.7; 3270 0.2; 3597 -0.1; 3957 -0.6; 4353 0.1; 4788 2.8; 5267 5.8; 5793 6.0; 6373 5.5; 7010 2.2; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Oppo PM3 sample C GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oppo PM3 sample C ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 1.03 | 2.5 dB  |
| Peaking | 61 Hz    | 2.03 | 1.6 dB  |
| Peaking | 378 Hz   | 2.19 | 4.0 dB  |
| Peaking | 2070 Hz  | 1.58 | -2.9 dB |
| Peaking | 5741 Hz  | 3.26 | 7.0 dB  |
| Peaking | 136 Hz   | 2.25 | -3.2 dB |
| Peaking | 143 Hz   | 0.84 | 1.7 dB  |
| Peaking | 198 Hz   | 3.54 | -1.9 dB |
| Peaking | 24000 Hz | 1.83 | 0.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Oppo%20PM3%20sample%20C/Oppo%20PM3%20sample%20C.png)