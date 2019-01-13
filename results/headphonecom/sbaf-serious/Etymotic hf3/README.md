# Etymotic hf3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 5.9; 37 5.7; 41 5.4; 45 5.1; 49 4.8; 54 4.5; 60 4.1; 66 3.8; 72 3.4; 79 2.9; 87 2.6; 96 2.3; 106 2.1; 116 1.8; 128 1.5; 141 1.0; 155 0.8; 170 0.6; 187 0.5; 206 0.4; 227 0.4; 249 0.3; 274 0.4; 302 0.4; 332 0.6; 365 0.8; 402 1.0; 442 0.9; 486 1.0; 535 1.2; 588 1.4; 647 1.6; 712 1.6; 783 1.4; 861 1.0; 947 0.4; 1042 -0.2; 1146 -0.9; 1261 -1.6; 1387 -2.5; 1526 -3.3; 1678 -3.8; 1846 -4.0; 2031 -3.8; 2234 -3.4; 2457 -2.4; 2703 -1.0; 2973 1.2; 3270 3.7; 3597 5.4; 3957 5.3; 4353 4.2; 4788 4.6; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic hf3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic hf3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.43 | 6.1 dB  |
| Peaking | 852 Hz  | 0.8  | 4.7 dB  |
| Peaking | 2275 Hz | 0.43 | -7.8 dB |
| Peaking | 3567 Hz | 1.6  | 10.3 dB |
| Peaking | 5803 Hz | 2.26 | 7.4 dB  |
| Peaking | 195 Hz  | 2.61 | -0.4 dB |
| Peaking | 940 Hz  | 6.73 | -0.2 dB |
| Peaking | 7696 Hz | 1.47 | 0.9 dB  |
| Peaking | 7731 Hz | 4.07 | -1.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Etymotic%20hf3/Etymotic%20hf3.png)