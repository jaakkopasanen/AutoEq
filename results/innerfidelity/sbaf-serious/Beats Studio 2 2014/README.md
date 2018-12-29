# Beats Studio 2 2014
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 4.7; 25 3.7; 28 2.2; 31 1.2; 34 0.7; 37 0.5; 41 0.4; 45 0.3; 49 0.3; 54 0.2; 60 0.2; 66 0.1; 72 -0.0; 79 -0.2; 87 -0.5; 96 -0.7; 106 -0.6; 116 -0.3; 128 -0.1; 141 0.3; 155 0.5; 170 0.9; 187 1.3; 206 1.7; 227 2.3; 249 2.9; 274 3.7; 302 4.7; 332 5.9; 365 6.0; 402 6.0; 442 6.0; 486 6.0; 535 6.0; 588 5.7; 647 2.6; 712 -0.2; 783 -1.3; 861 -1.3; 947 -0.3; 1042 -0.0; 1146 0.2; 1261 -0.3; 1387 0.3; 1526 1.0; 1678 1.4; 1846 2.8; 2031 3.9; 2234 4.7; 2457 5.2; 2703 4.9; 2973 3.7; 3270 0.9; 3597 1.3; 3957 3.4; 4353 5.6; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -1.2; 10263 -1.2; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats Studio 2 2014 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Studio 2 2014 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 2.45 | 5.5 dB  |
| Peaking | 465 Hz  | 0.98 | 7.5 dB  |
| Peaking | 800 Hz  | 2.05 | -4.9 dB |
| Peaking | 2386 Hz | 2.59 | 5.0 dB  |
| Peaking | 5270 Hz | 2.22 | 6.7 dB  |
| Peaking | 104 Hz  | 1.61 | -1.1 dB |
| Peaking | 320 Hz  | 5.98 | 1.1 dB  |
| Peaking | 3405 Hz | 8.37 | -2.3 dB |
| Peaking | 6954 Hz | 0.69 | 1.0 dB  |
| Peaking | 9277 Hz | 2.02 | -2.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beats%20Studio%202%202014/Beats%20Studio%202%202014.png)