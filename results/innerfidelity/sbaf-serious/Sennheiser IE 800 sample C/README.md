# Sennheiser IE 800 sample C
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -2.7; 23 -2.8; 25 -2.9; 28 -3.0; 31 -3.1; 34 -3.2; 37 -3.2; 41 -3.4; 45 -3.5; 49 -3.5; 54 -3.7; 60 -3.8; 66 -4.0; 72 -4.1; 79 -4.3; 87 -4.5; 96 -4.7; 106 -4.6; 116 -4.6; 128 -4.6; 141 -4.5; 155 -4.4; 170 -4.2; 187 -3.9; 206 -3.6; 227 -3.2; 249 -3.0; 274 -2.5; 302 -2.2; 332 -1.8; 365 -1.4; 402 -1.1; 442 -0.6; 486 -0.4; 535 -0.0; 588 0.5; 647 0.6; 712 0.6; 783 0.8; 861 0.6; 947 0.3; 1042 -0.1; 1146 -0.3; 1261 -0.6; 1387 -0.3; 1526 -0.7; 1678 -0.5; 1846 0.4; 2031 1.8; 2234 3.5; 2457 5.7; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 5.6; 5267 4.0; 5793 1.5; 6373 4.8; 7010 2.5; 7711 0.3; 8482 -0.8; 9330 -4.9; 10263 -7.2; 11289 -4.2; 12418 -0.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser IE 800 sample C GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser IE 800 sample C ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 44 Hz    | 0.31 | -3.1 dB |
| Peaking | 150 Hz   | 0.73 | -3.0 dB |
| Peaking | 2677 Hz  | 3.41 | 4.1 dB  |
| Peaking | 4259 Hz  | 1.19 | 6.0 dB  |
| Peaking | 10170 Hz | 3.54 | -8.6 dB |
| Peaking | 684 Hz   | 2.22 | 1.1 dB  |
| Peaking | 1536 Hz  | 2.88 | -1.7 dB |
| Peaking | 5816 Hz  | 7.81 | -2.6 dB |
| Peaking | 6520 Hz  | 8.02 | 3.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20IE%20800%20sample%20C/Sennheiser%20IE%20800%20sample%20C.png)