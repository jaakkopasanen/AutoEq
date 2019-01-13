# Blue MOFI Active On
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.4; 25 2.1; 28 1.9; 31 1.6; 34 1.5; 37 1.3; 41 1.2; 45 1.1; 49 1.0; 54 0.8; 60 0.6; 66 0.4; 72 0.2; 79 -0.1; 87 -0.4; 96 -0.9; 106 -1.0; 116 -0.9; 128 -1.1; 141 -1.8; 155 -2.2; 170 -1.3; 187 -1.9; 206 -1.9; 227 -1.5; 249 -0.8; 274 0.2; 302 1.1; 332 1.3; 365 1.2; 402 1.2; 442 3.1; 486 3.4; 535 3.0; 588 2.8; 647 2.4; 712 1.8; 783 1.5; 861 0.9; 947 0.3; 1042 -0.0; 1146 -0.2; 1261 -0.1; 1387 -0.3; 1526 -0.6; 1678 -0.5; 1846 0.1; 2031 1.3; 2234 2.2; 2457 2.4; 2703 3.5; 2973 4.1; 3270 4.4; 3597 5.4; 3957 3.4; 4353 -0.2; 4788 4.8; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Blue MOFI Active On GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Blue MOFI Active On ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 14 Hz   | 0.43 | 2.9 dB  |
| Peaking | 167 Hz  | 1.11 | -2.3 dB |
| Peaking | 500 Hz  | 1.58 | 3.6 dB  |
| Peaking | 3198 Hz | 2.42 | 4.7 dB  |
| Peaking | 5726 Hz | 3.2  | 6.4 dB  |
| Peaking | 709 Hz  | 4.44 | 0.5 dB  |
| Peaking | 1468 Hz | 2.57 | -1.2 dB |
| Peaking | 4184 Hz | 3.02 | 3.8 dB  |
| Peaking | 4263 Hz | 8.68 | -8.0 dB |
| Peaking | 8262 Hz | 3.73 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Blue%20MOFI%20Active%20On/Blue%20MOFI%20Active%20On.png)