# Akai MPC
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 3.4; 25 3.3; 28 3.2; 31 3.1; 34 3.0; 37 3.0; 41 2.9; 45 2.9; 49 2.9; 54 2.9; 60 2.6; 66 2.3; 72 2.2; 79 2.1; 87 2.0; 96 1.4; 106 0.2; 116 0.4; 128 0.4; 141 -0.2; 155 -0.6; 170 0.5; 187 -0.2; 206 0.2; 227 0.2; 249 0.8; 274 1.3; 302 1.5; 332 1.5; 365 1.5; 402 1.6; 442 1.5; 486 1.2; 535 1.3; 588 1.5; 647 1.5; 712 1.1; 783 1.1; 861 0.6; 947 0.1; 1042 -0.1; 1146 -0.2; 1261 -0.4; 1387 -1.2; 1526 -0.6; 1678 -1.2; 1846 0.5; 2031 1.9; 2234 1.7; 2457 1.5; 2703 2.7; 2973 3.7; 3270 1.5; 3597 0.8; 3957 2.4; 4353 3.4; 4788 5.6; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Akai MPC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Akai MPC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 0.8  | 3.3 dB  |
| Peaking | 60 Hz   | 1.49 | 2.0 dB  |
| Peaking | 428 Hz  | 1.22 | 1.7 dB  |
| Peaking | 2828 Hz | 4.42 | 3.0 dB  |
| Peaking | 5455 Hz | 2.39 | 6.8 dB  |
| Peaking | 708 Hz  | 3.35 | 0.8 dB  |
| Peaking | 1712 Hz | 1.77 | -2.1 dB |
| Peaking | 2017 Hz | 4.29 | 3.2 dB  |
| Peaking | 6512 Hz | 6.8  | 2.5 dB  |
| Peaking | 7706 Hz | 2.25 | -1.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Akai%20MPC/Akai%20MPC.png)