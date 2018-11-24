# MrSpeakers Alpha Prime

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 -0.1; 25 -0.3; 28 -0.4; 31 -0.4; 34 -0.5; 37 -0.6; 41 -0.7; 45 -0.6; 49 -0.6; 54 -0.8; 60 -0.9; 66 -0.8; 72 -0.9; 79 -1.0; 87 -1.2; 96 -1.2; 106 -1.0; 116 -0.8; 128 -0.9; 141 -1.6; 155 -1.4; 170 -0.3; 187 -0.6; 206 -0.9; 227 -0.7; 249 -0.9; 274 -0.9; 302 -0.8; 332 -0.9; 365 -0.9; 402 -0.4; 442 -0.1; 486 -0.7; 535 -0.5; 588 -0.1; 647 0.8; 712 0.3; 783 -0.2; 861 -0.6; 947 -0.6; 1042 0.2; 1146 0.2; 1261 0.8; 1387 1.1; 1526 1.1; 1678 1.4; 1846 3.1; 2031 4.5; 2234 4.9; 2457 5.1; 2703 5.2; 2973 5.8; 3270 6.0; 3597 6.0; 3957 6.0; 4353 4.7; 4788 1.8; 5267 1.0; 5793 0.7; 6373 0.1; 7010 1.8; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MrSpeakers Alpha Prime GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MrSpeakers Alpha Prime ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 119 Hz   | 0.32 | -1.0 dB |
| Peaking | 672 Hz   | 5.37 | 2.0 dB  |
| Peaking | 782 Hz   | 1.48 | -1.2 dB |
| Peaking | 3007 Hz  | 1.14 | 6.5 dB  |
| Peaking | 21894 Hz | 1.1  | -0.7 dB |
| Peaking | 2106 Hz  | 5.74 | 1.5 dB  |
| Peaking | 2925 Hz  | 3.27 | -0.7 dB |
| Peaking | 3921 Hz  | 3.87 | 1.1 dB  |
| Peaking | 4229 Hz  | 4.74 | 3.7 dB  |
| Peaking | 4487 Hz  | 1.64 | -2.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/MrSpeakers%20Alpha%20Prime/MrSpeakers%20Alpha%20Prime.png)