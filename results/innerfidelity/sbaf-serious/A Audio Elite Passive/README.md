# A Audio Elite Passive
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.0dB
GraphicEQ: 21 -1.8; 23 -1.9; 25 -2.0; 28 -2.1; 31 -2.2; 34 -2.2; 37 -2.2; 41 -2.2; 45 -2.2; 49 -2.2; 54 -2.1; 60 -2.1; 66 -2.0; 72 -1.8; 79 -1.8; 87 -2.1; 96 -2.3; 106 -2.5; 116 -2.4; 128 -3.0; 141 -3.3; 155 -2.8; 170 -1.9; 187 -2.1; 206 -1.1; 227 0.1; 249 0.9; 274 1.4; 302 1.8; 332 1.9; 365 1.9; 402 1.5; 442 1.2; 486 0.7; 535 0.3; 588 0.8; 647 1.2; 712 0.6; 783 -0.3; 861 -0.4; 947 -0.1; 1042 0.2; 1146 0.5; 1261 0.9; 1387 1.1; 1526 1.0; 1678 1.0; 1846 1.6; 2031 2.6; 2234 3.6; 2457 4.3; 2703 4.7; 2973 4.5; 3270 3.8; 3597 3.2; 3957 1.1; 4353 -0.9; 4788 -0.2; 5267 3.1; 5793 5.6; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`A Audio Elite Passive GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-59**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `A Audio Elite Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 0.49 | -2.1 dB |
| Peaking | 149 Hz  | 1.08 | -3.2 dB |
| Peaking | 305 Hz  | 1.27 | 2.8 dB  |
| Peaking | 2675 Hz | 2    | 5.0 dB  |
| Peaking | 6103 Hz | 5    | 6.3 dB  |
| Peaking | 3536 Hz | 5.48 | 1.7 dB  |
| Peaking | 3845 Hz | 3.78 | 0.3 dB  |
| Peaking | 4516 Hz | 3.55 | -3.6 dB |
| Peaking | 5276 Hz | 4.43 | 2.2 dB  |
| Peaking | 8327 Hz | 4.4  | -0.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/A%20Audio%20Elite%20Passive/A%20Audio%20Elite%20Passive.png)