# Philips Construct
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -1.1; 23 -1.1; 25 -1.1; 28 -1.2; 31 -1.2; 34 -1.2; 37 -1.1; 41 -1.0; 45 -0.8; 49 -0.7; 54 -0.4; 60 0.0; 66 0.2; 72 -0.0; 79 -0.8; 87 -1.8; 96 -2.4; 106 -2.1; 116 -2.2; 128 -2.3; 141 -1.9; 155 -1.1; 170 -0.6; 187 0.1; 206 1.1; 227 2.2; 249 3.5; 274 4.7; 302 5.4; 332 5.3; 365 4.5; 402 3.1; 442 1.8; 486 0.5; 535 -0.4; 588 -0.7; 647 -1.0; 712 -1.2; 783 -0.9; 861 -0.8; 947 -0.4; 1042 0.5; 1146 1.4; 1261 2.6; 1387 3.3; 1526 3.9; 1678 4.7; 1846 5.8; 2031 6.0; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips Construct GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips Construct ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 1.49 | -1.3 dB |
| Peaking | 124 Hz  | 1.37 | -2.9 dB |
| Peaking | 315 Hz  | 1.55 | 6.4 dB  |
| Peaking | 721 Hz  | 1    | -3.5 dB |
| Peaking | 2835 Hz | 0.53 | 6.9 dB  |
| Peaking | 67 Hz   | 5.17 | 0.9 dB  |
| Peaking | 1877 Hz | 4.14 | 0.9 dB  |
| Peaking | 2893 Hz | 2.08 | -0.9 dB |
| Peaking | 6191 Hz | 1.95 | 5.4 dB  |
| Peaking | 7535 Hz | 1.39 | -4.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20Construct/Philips%20Construct.png)