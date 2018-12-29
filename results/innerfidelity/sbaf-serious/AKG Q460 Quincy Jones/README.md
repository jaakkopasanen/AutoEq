# AKG Q460 Quincy Jones
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 4.7; 25 4.1; 28 3.3; 31 2.7; 34 2.2; 37 1.8; 41 1.5; 45 1.2; 49 1.0; 54 0.8; 60 0.5; 66 0.3; 72 0.2; 79 -0.1; 87 -0.4; 96 -0.7; 106 -0.8; 116 -1.2; 128 -1.6; 141 -1.9; 155 -2.2; 170 -2.3; 187 -2.6; 206 -2.6; 227 -2.6; 249 -2.8; 274 -2.8; 302 -2.9; 332 -3.1; 365 -3.0; 402 -2.5; 442 -2.3; 486 -2.4; 535 -1.8; 588 -0.1; 647 1.7; 712 2.7; 783 3.7; 861 2.8; 947 0.9; 1042 0.1; 1146 0.2; 1261 0.2; 1387 0.8; 1526 2.0; 1678 3.3; 1846 4.9; 2031 5.9; 2234 6.0; 2457 6.0; 2703 6.0; 2973 5.4; 3270 2.9; 3597 0.4; 3957 0.3; 4353 0.8; 4788 3.6; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG Q460 Quincy Jones GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG Q460 Quincy Jones ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 12 Hz   | 0.64 | 8.1 dB  |
| Peaking | 757 Hz  | 1.98 | 7.0 dB  |
| Peaking | 1081 Hz | 0.15 | -4.6 dB |
| Peaking | 2259 Hz | 1.19 | 10.6 dB |
| Peaking | 5781 Hz | 2.62 | 8.1 dB  |
| Peaking | 1881 Hz | 3.94 | 0.9 dB  |
| Peaking | 2291 Hz | 2.82 | -1.5 dB |
| Peaking | 2911 Hz | 4.3  | 2.4 dB  |
| Peaking | 3766 Hz | 4.22 | -2.1 dB |
| Peaking | 9180 Hz | 0.25 | 0.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20Q460%20Quincy%20Jones/AKG%20Q460%20Quincy%20Jones.png)