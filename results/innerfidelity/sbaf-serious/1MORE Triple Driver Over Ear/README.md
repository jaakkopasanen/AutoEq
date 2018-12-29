# 1MORE Triple Driver Over Ear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.4dB
GraphicEQ: 21 -0.6; 23 -1.0; 25 -1.4; 28 -2.0; 31 -2.5; 34 -2.9; 37 -3.2; 41 -3.4; 45 -3.6; 49 -3.7; 54 -3.8; 60 -3.6; 66 -3.2; 72 -3.1; 79 -3.8; 87 -4.2; 96 -3.8; 106 -3.5; 116 -3.7; 128 -3.7; 141 -3.2; 155 -2.5; 170 -1.7; 187 -1.1; 206 -0.4; 227 0.6; 249 1.4; 274 2.1; 302 2.6; 332 3.0; 365 2.9; 402 2.5; 442 1.8; 486 0.6; 535 -0.2; 588 -0.3; 647 -0.5; 712 -0.8; 783 -0.7; 861 -0.8; 947 -0.5; 1042 0.1; 1146 -0.0; 1261 0.2; 1387 0.2; 1526 0.2; 1678 0.6; 1846 1.3; 2031 1.8; 2234 2.1; 2457 3.0; 2703 3.3; 2973 2.9; 3270 2.6; 3597 1.6; 3957 -1.4; 4353 -1.2; 4788 0.0; 5267 1.8; 5793 1.5; 6373 0.7; 7010 1.7; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`1MORE Triple Driver Over Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-34**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `1MORE Triple Driver Over Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 160 Hz  | 0.2  | -5.0 dB |
| Peaking | 318 Hz  | 0.94 | 7.6 dB  |
| Peaking | 3002 Hz | 1.07 | 4.0 dB  |
| Peaking | 4157 Hz | 3.27 | -4.5 dB |
| Peaking | 5393 Hz | 3.53 | 1.5 dB  |
| Peaking | 17 Hz   | 1.16 | 1.4 dB  |
| Peaking | 42 Hz   | 1.12 | -0.7 dB |
| Peaking | 69 Hz   | 3.73 | 1.3 dB  |
| Peaking | 83 Hz   | 3.77 | -0.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/1MORE%20Triple%20Driver%20Over%20Ear/1MORE%20Triple%20Driver%20Over%20Ear.png)